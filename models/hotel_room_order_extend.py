from odoo import models, api, fields

class RoomOrderExtend(models.Model):
    _inherit = 'hotels.room.order'

    order_sale_quotation = fields.Many2one('sale.order', string="Room Booking Quotation")
    order_service_product_ids = fields.One2many('room.order.service.product', 'order_id', string="Service Products")

    @api.model
    def create(self, vals):
        record = super(RoomOrderExtend, self).create(vals)

        # Prepare the order line for the room
        room_line = {
            'product_id': record.room_id.product_id.product_variant_ids[0].id,
            'product_uom_qty': (record.check_out_date - record.check_in_date).days,  # Room quantity
            'price_unit': record.room_id.room_price,  # Room price
        }

        # Create the quotation
        quotation_vals = {
            'partner_id': 47,  # Replace with the correct partner_id logic
            'order_line': [(0, 0, room_line)],
        }

        record.order_sale_quotation = self.env['sale.order'].create(quotation_vals)

        # Add service product lines to the created quotation
        if record.order_sale_quotation:
            service_lines = [
                (0, 0, {
                    'product_id': service_product.product_id.id,
                    'product_uom_qty': service_product.quantity,
                    'price_unit': service_product.price_unit,
                }) for service_product in record.order_service_product_ids
            ]
            record.order_sale_quotation.write({
                'order_line': [(4, line.id) for line in record.order_sale_quotation.order_line] + service_lines,
                'note': 'Updated note for the sale order',
            })

        return record

    def write(self, vals):
        # Update the room order
        result = super(RoomOrderExtend, self).write(vals)

        # Loop through the records being updated (if batch update)
        for record in self:
            sale_order = self.env['sale.order'].search([('id', '=', record.order_sale_quotation.id)])

            if sale_order:
                # Get the product variant or fallback to product template
                product_variant = record.room_id.product_id.product_variant_ids and \
                                  record.room_id.product_id.product_variant_ids[0] or record.room_id.product_id

                # Update sale order's order lines (quotation lines) if the room order has changed
                for line in sale_order.order_line:
                    line.product_id = product_variant.id
                    line.product_uom_qty = (record.check_out_date - record.check_in_date).days
                    line.price_unit = record.room_id.room_price

        return result
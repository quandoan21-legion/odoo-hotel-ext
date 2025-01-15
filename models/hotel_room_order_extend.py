from odoo import models, api, fields


class RoomOrderExtend(models.Model):
    _inherit = 'hotels.room.order'

    order_sale_quotation = fields.Many2one('sale.order', string="Room Booking Quotation")

    @api.model
    def create(self, vals):
        record = super(RoomOrderExtend, self).create(vals)
        product_variant = record.room_id.product_id.product_variant_ids and \
                          record.room_id.product_id.product_variant_ids[0] or record.room_id.product_id
        quotation_vals = {
            'partner_id': 47,
            'order_line': [(0, 0, {
                'product_id': product_variant.id,
                'product_uom_qty': (record.check_out_date - record.check_in_date).days,  # Room quantity
                'price_unit': record.room_id.room_price,  # Price of the room
            })],
        }
        record.order_sale_quotation = self.env['sale.order'].create(quotation_vals)
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
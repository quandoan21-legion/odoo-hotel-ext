import logging

from odoo import models, fields, api

class RoomOrderExtend(models.Model):
    _inherit = 'hotels.room.order'

    _logger = logging.getLogger(__name__)
    order_sale_quotation = fields.Many2one('sale.order', string="Room Booking Quotation")
    order_service_product_ids = fields.One2many('room.order.service.product', 'order_id', string="Service Products")

    def action_report_room_order(self):
        context = {
            'doc': self,  # 'self' refers to the current record of 'hotels.room.order'
        }

        # Trigger the report and pass the context
        return self.env.ref('hotel_ext.action_report_room_order').report_action(self, data=context)

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
        record.update_order_line()

        return record

    def write(self, vals):
        # Update the room order
        result = super(RoomOrderExtend, self).write(vals)

        self.update_order_line()

        return result

    def update_order_line(self):
        for record in self:
            if record.order_sale_quotation:
                # Prepare service lines
                service_lines = [
                    (0, 0, {
                        'product_id': service_product.product_id.id,
                        'product_uom_qty': service_product.quantity,
                        'price_unit': service_product.price_unit,
                    }) for service_product in record.order_service_product_ids
                ]

                # Add new service lines
                record.order_sale_quotation.write({
                    'order_line': [(4, line.id) for line in record.order_sale_quotation.order_line] + service_lines,
                })

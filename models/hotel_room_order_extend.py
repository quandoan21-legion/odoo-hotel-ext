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
        # Ensure the partner_id is passed correctly
        record = super(RoomOrderExtend, self).create(vals)

        # Prepare the order line for the room
        room_line = {
            'product_id': record.room_id.product_id.product_variant_ids[0].id,
            'product_uom_qty': (record.check_out_date - record.check_in_date).days,  # Room quantity
            'price_unit': record.room_id.room_price,  # Room price
        }

        # Get partner_id from customer_name (the Many2one relation)
        partner_id = record.customer_name.id  # This will get the partner associated with the room order

        # Create the quotation with the correct partner_id
        quotation_vals = {
            'partner_id': partner_id,  # Use the partner_id from the customer_name field
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
                # Get partner_id from customer_name (the Many2one relation)
                partner_id = record.customer_name.id  # This will get the partner associated with the room order

                # Extract existing order lines from the quotation
                existing_lines = {line.product_id.id: line for line in record.order_sale_quotation.order_line}

                # Prepare service lines for the room order
                service_lines = []
                for service_product in record.order_service_product_ids:
                    service_line = {
                        'product_id': service_product.product_id.id,
                        'product_uom_qty': service_product.quantity,
                        'price_unit': service_product.price_unit,
                    }

                    # Check if the service product already exists in the quotation
                    if service_product.product_id.id in existing_lines:
                        # If it exists, we update the quantity and price
                        existing_lines[service_product.product_id.id].write({
                            'product_uom_qty': service_product.quantity,
                            'price_unit': service_product.price_unit,
                        })
                    else:
                        # If it doesn't exist, we create a new order line for this service
                        service_lines.append((0, 0, service_line))

                record.order_sale_quotation.write({
                    'partner_id': partner_id,  # Update the partner_id in the quotation
                })

                # Add new service lines (if any)
                if service_lines:
                    record.order_sale_quotation.write({
                        'order_line': [(4, line.id) for line in record.order_sale_quotation.order_line] + service_lines
                    })

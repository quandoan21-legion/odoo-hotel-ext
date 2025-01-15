from odoo import fields, models, api


class RoomExtend(models.Model):
    _inherit = 'hotels.room'

    product_id = fields.Many2one('product.template', string="Related Product")

    @api.model
    def create(self, vals):
        # Create a new record in your custom model
        record = super(RoomExtend, self).create(vals)

        # Create a corresponding product.template record in the Sales module
        product_vals = {
            'name': record.name,
            'list_price': record.room_price,
            'type': 'service',  # Adjust product type as needed
        }
        product = self.env['product.template'].create(product_vals)

        # Link the created product to the custom record
        record.product_id = product.id

        return record

    def write(self, vals):
        # Perform updates in the custom model
        result = super(RoomExtend, self).write(vals)

        # Update the corresponding product.template record if necessary
        for record in self:
            if record.product_id:
                product_vals = {}
                if 'name' in vals:
                    product_vals['name'] = vals['name']
                if 'room_price' in vals:
                    product_vals['list_price'] = vals['room_price']

                if product_vals:
                    record.product_id.write(product_vals)

        return result

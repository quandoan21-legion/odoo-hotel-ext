from odoo import fields, models, api


class RoomOrderServiceProduct(models.Model):
    _name = 'room.order.service.product'
    _description = 'Room Order Product Line'

    order_id = fields.Many2one('hotels.room.order', string="Room Order", required=True)
    product_id = fields.Many2one('product.product', string="Product", domain="[('categ_id.name', '=', 'Hotel Services')]", required=True)
    quantity = fields.Integer(string="Quantity", default=1)
    price_unit = fields.Float(string="Unit Price", related='product_id.list_price', readonly=True)
    subtotal = fields.Float(string="Subtotal", compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit

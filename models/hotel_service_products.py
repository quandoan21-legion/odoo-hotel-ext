from odoo import models, fields


class HotelServiceProducts(models.Model):
    _name = "hotels.service.products"
    _description = "Hotel Products for sell (Food, drink, etc....)"

    name = fields.Char(string="Product Name", required="True")
    ordered_qty = fields.Integer(string="Quantity That Customer Ordered")
    room_order_id = fields.Many2one('hotels.room.order')



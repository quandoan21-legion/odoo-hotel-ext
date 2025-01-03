from odoo import models, fields

class HotelExtend(models.Model):
    _inherit = 'hotels.hotel'

    room_order_history_ids = fields.One2many(
        'hotels.room.order.history', 'hotel_id', string="Room Order History"
    )

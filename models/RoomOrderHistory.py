from odoo import models, fields

class RoomOrderHistory(models.Model):
    _name = 'hotels.room.order.history'
    _description = 'Room Order History'

    hotel_id = fields.Many2one('hotels.hotel', string="Hotel", ondelete='cascade')
    room_id = fields.Many2one('hotels.room', string="Room")
    customer_name = fields.Char(string="Customer Name")
    check_in_date = fields.Date(string="Check-In Date")
    check_out_date = fields.Date(string="Check-Out Date")
    order_id = fields.Many2one('hotels.room.order', string="Order")

from odoo import models, fields

class RoomOrderHistory(models.Model):
    _name = 'hotels.room.order.history'
    _description = 'Room Order History'

    room_id = fields.Many2one('hotels.room', string='Room')
    order_id = fields.Many2one('hotels.room.order', string='Room Order', required=True)
    customer_name = fields.Char(related='order_id.customer_name', string='Customer Name', store=True)
    check_in_date = fields.Date(related='order_id.check_in_date', string='Check In Date', store=True)
    check_out_date = fields.Date(related='order_id.check_out_date', string='Check Out Date', store=True)

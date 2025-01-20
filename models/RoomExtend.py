from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ExtendRoom(models.Model):
    _inherit = 'hotels.room'

    room_width = fields.Float(string='Room Width', default=1.0)
    room_length = fields.Float(string='Room Length', default=1.0)
    room_size = fields.Float(string='Room Size(SQM)', compute='_compute_room_size', store=True)
    room_capacity = fields.Integer(string='Room Capacity', default=1)
    room_allow_smoke = fields.Boolean(string='Allow Smoke')


    @api.depends('room_width', 'room_length')
    def _compute_room_size(self):
        for record in self:
            record.room_size = record.room_width * record.room_length

    @api.constrains('room_capacity')
    def check_room_capacity(self):
        for record in self:
            if record.room_capacity < 0:
                raise ValidationError('Room capacity cannot be less than 0.')

    @api.constrains('room_width', 'room_length')
    def check_room_size(self):
        for record in self:
            if record.room_width < 0 or record.room_length < 0:
                raise ValidationError('Room dimensions cannot be less than 0.')


from odoo import models, api

class RoomOrderExtend(models.Model):
    _inherit = 'hotels.room.order'  # Inherit from RoomOrder model

    @api.model
    def create(self, vals):
        # Perform custom logic here before creating the record
        new_order = super(RoomOrderExtend, self).create(vals)
        # Create a RoomOrderHistory record after creating the RoomOrder
        self.env['hotels.room.order.history'].create({
            'hotel_id': new_order.room_id.hotel_id.id,
            'room_id': new_order.room_id.id,
            'customer_name': new_order.customer_name,
            'check_in_date': new_order.check_in_date,
            'check_out_date': new_order.check_out_date,
            'order_id': new_order.id,  # Link the order history to the order
        })

        return new_order

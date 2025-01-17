# report/room_order_report.py
from odoo import api, models

class RoomOrderReport(models.AbstractModel):
    _name = 'report.hotel_ext.report_room_order'
    _description = 'Room Order Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': docids,
            'doc_model': 'hotels.room.order',
            'docs': self.env['hotels.room.order'].browse(docids),
            'data': data,
        }
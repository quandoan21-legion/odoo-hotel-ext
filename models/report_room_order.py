from odoo import api, fields, models

class CustomReport(models.AbstractModel):
    _name = 'report.hotel_ext.report_template_id'
    _description = 'Custom Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['your.model'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hotels.room.order',
            'docs': docs,
            'data': data,
        }

from odoo import models, fields, api
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # Define discount as a fixed amount field (e.g., $10 off)
    x_discount = fields.Float(string="Discount Amount", default=0.0)

    def _prepare_base_line_for_taxes_computation(self, **kwargs):
        """ Convert the current record to a dictionary in order to use the generic taxes computation method
        defined on account.tax.

        :return: A python dictionary.
        """
        if self.x_discount > self.price_unit:
            raise UserError("The discount amount mustn't bigger than your unit price")
            self.x_discount = 0

        price_unit = self.price_unit - self.x_discount
        self.ensure_one()
        return super()._prepare_base_line_for_taxes_computation(**
            {
                'price_unit': price_unit,
                **kwargs
            }
        )

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'x_discount')
    def _compute_amount(self):
        for line in self:
            base_line = line._prepare_base_line_for_taxes_computation()
            self.env['account.tax']._add_tax_details_in_base_line(base_line, line.company_id)
            line.price_subtotal = base_line['tax_details']['raw_total_excluded_currency']
            line.price_total = base_line['tax_details']['raw_total_included_currency']
            line.price_tax = line.price_total - line.price_subtotal

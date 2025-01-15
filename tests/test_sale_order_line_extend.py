from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError

class TestSaleOrderLine(TransactionCase):
    def setUp(self):
        super(TestSaleOrderLine, self).setUp()
        # Create a test product
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'list_price': 100.0,
            'standard_price': 80.0,
        })

        # Create a sale order line
        self.sale_order_line = self.env['sale.order.line'].create({
            'product_id': self.product.id,
            'price_unit': 50.0,
            'product_uom_qty': 1,
        })

    def test_valid_discount(self):
        """Test applying a valid discount."""
        self.sale_order_line.x_discount = 10.0  # Valid discount
        base_line = self.sale_order_line._prepare_base_line_for_taxes_computation()
        self.assertEqual(
            base_line['price_unit'],
            40.0,
            "Price unit after discount should be correctly calculated."
        )

    def test_invalid_discount(self):
        """Test applying an invalid discount."""
        self.sale_order_line.x_discount = 60.0  # Invalid discount (greater than price_unit)
        with self.assertRaises(UserError, msg="The discount amount mustn't bigger than your unit price"):
            self.sale_order_line._prepare_base_line_for_taxes_computation()

    def test_compute_amount_with_discount(self):
        """Test the computation of amount with a valid discount."""
        self.sale_order_line.x_discount = 10.0  # Valid discount
        self.sale_order_line._compute_amount()  # Trigger the computation
        self.assertEqual(
            self.sale_order_line.price_subtotal,
            40.0,  # Expected subtotal
            "Subtotal should be calculated correctly after applying discount."
        )

    def test_compute_amount_without_discount(self):
        """Test the computation of amount without any discount."""
        self.sale_order_line.x_discount = 0.0  # No discount
        self.sale_order_line._compute_amount()  # Trigger the computation
        self.assertEqual(
            self.sale_order_line.price_subtotal,
            50.0,  # Expected subtotal
            "Subtotal should remain unchanged when no discount is applied."
        )

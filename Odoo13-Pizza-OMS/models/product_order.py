from odoo import fields, models, api


class ProductOrder(models.Model):
    _name = 'product.order'

    order_id = fields.Many2one('pizza.management', 'Order')
    product_id = fields.Many2one('product.inventory', 'Product Name')
    qty = fields.Integer('Quantity', default='1')
    price = fields.Float(
        'Price', related='product_id.price')

    total_price = fields.Float(
        'Total Price', compute='_compute_product_total_price')

    total_bill = fields.Float('Total Bill')

    def _compute_product_total_price(self):
        price = 0.0
        for rec in self:
            if rec.qty == 1:
                rec.total_price = rec.price
            elif rec.qty > 1:
                rec.total_price = rec.qty * rec.price
            price += rec.total_price
        self.total_bill = price

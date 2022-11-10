from odoo import fields, models


class ProductInventory(models.Model):
    _name = 'product.inventory'

    PRODUCT_TYPE = [('dessert', 'Dessert'), ('drink', 'Drink'),
                    ('food', 'Food'), ('other', 'Other')]
    PRODUCT_SERVING = [('small', 'Small'), ('medium', 'Medium'),
                       ('large', 'Large')]

    name = fields.Char('Product Name', required=True)
    serving = fields.Selection(PRODUCT_SERVING, string="Serving")
    type = fields.Selection(PRODUCT_TYPE, string="Type")
    price = fields.Float('Price', group_operator=False)

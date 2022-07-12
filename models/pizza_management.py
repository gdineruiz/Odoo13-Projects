from odoo import fields, models, api


class PizzaManagement(models.Model):
    _name = 'pizza.management'

    STATE_SELECTION = [('draft', 'Placed'), ('submit', 'Prepared'),
                       ('reserve', 'Delivered'), ('cancel', 'Cancelled')]

    name = fields.Char('Order Number')

    customer_id = fields.Many2one('customer.record', 'Customer')
    mobile = fields.Char('Mobile Number')
    email = fields.Char('Email Address')
    address1 = fields.Char('Address 1')
    address2 = fields.Char('Address 2')

    image = fields.Image('Profile Picture')

    special_remarks = fields.Text('Special Remarks')
    customer_description = fields.Text('Customer Description')

    product_id = fields.Many2one('product.inventory', 'Product Name')
    customer_order_ids = fields.One2many(
        'product.order', 'order_id', 'Guests')
    state = fields.Selection(STATE_SELECTION, string="Status", default="draft")
    image = fields.Image('Profile Picture')

    total_bill = fields.Float('Integer', related="customer_order_ids.total_bill")

    def draft(self):
        self.state = "draft"

    def submit(self):
        self.state = "submit"

    def cancel(self):
        self.state = "cancel"

    def reserve(self):
        self.state = "reserve"

    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code(
            'pizza.management') or 'ORDER-0000'
        vals['name'] = seq
        return super(PizzaManagement, self).create(vals)

    @api.onchange('customer_id')
    def onchange_customer_id(self):
        if self.customer_id:
            self.mobile = self.customer_id.mobile
            self.email = self.customer_id.email
            self.address1 = self.customer_id.address1
            self.address2 = self.customer_id.address2
            self.customer_description = self.customer_id.customer_description
            self.image = self.customer_id.image

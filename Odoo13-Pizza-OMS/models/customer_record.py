from odoo import models, fields


class CustomerRecord(models.Model):
    _name = 'customer.record'

    name = fields.Char('Customer Name')
    mobile = fields.Char('Mobile Number')
    email = fields.Char('Email Address')

    address1 = fields.Char('Address 1')
    address2 = fields.Char('Address 2')

    customer_description = fields.Text('Customer Description')

    image = fields.Image('Profile Picture')
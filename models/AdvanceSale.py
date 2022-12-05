

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'test1.advance_sale'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=False)



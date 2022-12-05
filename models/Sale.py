from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_code = fields.Char(string='Discount code', related='partner_id.discount_code')#partner_id is a many2one field
    discount_total = fields.Monetary(string='Discount', compute='_compute_total_payment')#Monetary kieu float co ku tu



    @api.depends("discount_code")
    def _compute_total_payment(self):
        for rec in self:
            if rec.discount_code and not rec.discount_code == '':
                discount_percent = int(rec.discount_code[4:len(rec.discount_code)])
                rec.discount_total = (rec.amount_untaxed * discount_percent) / 100
            else:
                rec.discount_total = 0
            amount_untaxed = amount_tax = 0.0
            for line in rec.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            rec.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax - rec.discount_total,
            })

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            check_name = self.search([('partner_id', '=', vals['partner_id'])])
        if not check_name:
            res_ids = super(SaleOrder, self).create(vals_list)
            return res_ids
        else:
            raise ValidationError(_("Customer already exist in database "))

    def name_get(self):  # default class can be shown in the author form
        result = []
        for rec in self:
            name = "%s-%s" % (rec.partner_id.name, rec.name)
            result.append((rec.id, name))  # return the many 2 one list
        return result

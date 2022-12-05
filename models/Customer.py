from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Customer(models.Model):
    _inherit = 'res.partner'  # ke thua tu res.partner

    # name = fields.Many2one('sale.order', string='Customer')
    # customer_id = fields.Many2one('sale.order', string='Customer_ID')
    # name = fields.Char(string="Customer")

    discount_code = fields.Char(string="Discount Code (format: VIP + ‘_’ + integer)", required=False)



    @api.onchange('discount_code')
    def onchange_discount_code(self):
        for rec in self:
            if rec.discount_code:
                if rec.discount_code.isdigit():
                    rec.discount_code = "VIP_" + str(rec.discount_code)
                else:
                    rec.discount_code = ''
                    raise ValidationError(_("The format is not correct please Type The number"))

    def write(self, value):
        user_pool = self.env['res.users']
        user = user_pool.browse(self._uid)
        advance_gr = user.has_group('test1.group_adavance_sale')

        if not advance_gr:
            if value.get('discount_code'):
                raise ValidationError(_("The field Discount Code only editable by the Advance Sale"))
        else:
            return super(Customer, self).write(value)

    def _display_customer_discount_code(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Customer',
            'res_model': 'res.partner',
            'domain': [('discount_code', '!=', False)],
            'view_mode': 'tree,form',
            'target': 'current',
        }




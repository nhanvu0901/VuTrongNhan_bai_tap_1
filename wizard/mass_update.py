from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, AccessError

from ..models.Customer import Customer


class MassUpdate(models.TransientModel):
    _name = 'mass.update.wizard'
    new_discount_code = fields.Char(string="Discount Code (format: VIP + ‘_’ + integer)", required=False)

    @api.onchange('new_discount_code')
    def onchange_discount_code(self):
        for rec in self:
            if rec.new_discount_code:
                if rec.new_discount_code.isdigit():
                    rec.new_discount_code = "VIP_" + str(rec.new_discount_code)
                else:
                    rec.new_discount_code = ''
                    raise ValidationError(_("The format is not correct please Type The number"))

    def action_confirm(self):
        for rec in self:
            selected_ids = rec.env.context.get('active_ids', [])
            selected_records = rec.env['res.partner'].browse(selected_ids)

            if rec.new_discount_code:

                selected_records.discount_code = rec.new_discount_code
            else:
                raise ValidationError(_("No Update"))



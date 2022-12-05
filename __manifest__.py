# -*- coding: utf-8 -*-
{
    'name': "VuTrongNhan_bai_tap_1",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'VuTrongNhan_bai_tap_1',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
        'sale'

    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_group.xml',
        'views/customer.xml',
        'views/advanceSale.xml',
        'views/sale.xml',
        'views/customer_discount_code.xml',
        'wizard/mass_update.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

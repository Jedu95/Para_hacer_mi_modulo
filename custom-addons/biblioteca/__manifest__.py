# -*- coding: utf-8 -*-
{
    'name': "Gestión de Biblioteca",
    'version': "16.0.1.0.0",
    'summary': "Realiza la gestión de nuestra biblioteca"  
    'description': """
        Long description of module's purpose
    """,

    'author': "José Eduardo Fernández Razo",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

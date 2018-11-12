# -*- coding: utf-8 -*-
{
    'name': "Gestion des formations.",

    'summary': """
        Ce module est destiné pour gérer un centre de formation avec Odoo11. 
        """,

    'description': """
        Ce module est destiné pour gérer un centre de formation.
    """,

    'author': "Aymen Bennour",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/formation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
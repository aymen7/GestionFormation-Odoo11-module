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
    'website': "https://github.com/aymen7/GestionFormation-Odoo11-module",
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/gestion_formation.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
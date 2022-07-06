# -*- coding: utf-8 -*-
{
    'name': "DC3",
    'version' : "1.0",

    'summary': """
        Evaluación de trabajos de riesgo""",

    'description': """
        Permite cordina trabajos de alto riesgo llevando control de tareas de seguridad
    """,

    'author': "Javier Pineda Rodriguez",
    'website': "http://www.skillsdepot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],


    # always loaded
    'data': [
        'views/menus.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'qweb':[
    ],
    'application': True,
    'sequence': 1
}

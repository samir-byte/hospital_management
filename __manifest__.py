# -*- coding: utf-8 -*-

{
    'name' : 'Hospital management',
    'version' : '14.0.1.0',
    'summary': 'Hospital Management System',
    'sequence': 10,
    'description': """ This is my first odoo module related to hospital management system  """,
    'category': 'Productivity',
    'website': 'https://www.odoo.com/page/billing',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    
}

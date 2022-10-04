# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Envio Masivo',
    'version': '1.0',
    'author': 'Mit-Mut',
    'category': 'Sale',
    'website': 'https://www.mit-mut.com',
    'license': 'LGPL-3',
    'support': 'info@mit-mut.com',
    'summary': 'Envio masivo de sale order',
    'description': """
    Loren ipsum
    """,
    'website': 'www.mit-mut.com',
    'depends': ['base','sale','sale_management'],
    'data': [
        
        'wizard/so_bulk_mail.xml',
        'views/sale_action_menu.xml',  
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

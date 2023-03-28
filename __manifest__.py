# -*- coding: utf-8 -*- 


{
    'name': 'Point of sale lock',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Sales/Point of Sale',
    'demo': [],
    'depends': ['point_of_sale'],
    'data': [
        'security/pos_lock_security.xml',
        'views/pos_order_view.xml',
        'views/pos_session_view.xml'

    ],
    'license': 'LGPL-3',
}

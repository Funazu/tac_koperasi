# -*- coding: utf-8 -*-

{
    'name': "TAC Koperasi",
    'summary': """
     Sistem Koperasi
        """,
    'description': """
        Sistem Koperasi""",
    'author': "Teknologi Aplikasi Cerdas",
    'company': "Teknologi Aplikasi Cerdas",
    'maintainer': 'Teknologi Aplikasi Cerdas',
    'website': "",
    "license": "AGPL-3",
    'category': 'Education',
    'version': '15.0.1.0.0',
    'depends': ['base'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/membership_view.xml',
        'views/membership_fee_view.xml',
        'views/membership_registration_view.xml',
        'views/membership_share_capital_view.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
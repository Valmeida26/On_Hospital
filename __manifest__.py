# Copyright 2022 Odoo.com
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Hospital Management',
    'sumary': 'Hospital Management Software',
    'sequence': -10,
    'description': """Modulo de menu de hospital""",
    'category': 'Productivity',
    'version': '13.0',
    'license': 'AGPL-3',
    'author': 'Vinícius Neves',
    'website': 'www.lliege.com.br',
    'depends': ['sale',
                'mail',
                'website_slides',
                'hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',
        'views/sales.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',

    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

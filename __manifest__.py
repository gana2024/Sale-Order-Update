{
    'name': "Sale Order Update",
    'version': '1.0',
    'depends': ['sale', 'base'],
    'author': "Gana",
    'category': '',
    'description': "",
    'data': [
        'views/form_views.xml',
        'views/sale_kanban_views.xml',
        'views/sale_menu.xml',
        'report/sale_order_report_template.xml',
        'report/sale_order_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

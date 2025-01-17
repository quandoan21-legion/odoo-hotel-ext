# -*- coding: utf-8 -*-
{
    'name': "hotel_ext",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hotel','sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_templates.xml',
        'report/report_views.xml',
        'views/form_views/hotel_room_order_form_view_extend.xml',
        'views/form_views/sale_order_line_extend.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/form_views/view_hotel_form_extend.xml',
        'views/form_views/view_hotel_room_form_extend.xml',
        'views/list_views/view_hotel_room_list_extend.xml',
        'views/hotel_sevice_products/list_views/hotel_service_product_list_view.xml',
        'views/menus.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


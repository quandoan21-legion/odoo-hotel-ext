# -*- coding: utf-8 -*-
# from odoo import http


# class Hotel-ext(http.Controller):
#     @http.route('/hotel_ext/hotel_ext', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_ext/hotel_ext/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_ext.listing', {
#             'root': '/hotel_ext/hotel_ext',
#             'objects': http.request.env['hotel_ext.hotel_ext'].search([]),
#         })

#     @http.route('/hotel_ext/hotel_ext/objects/<model("hotel_ext.hotel_ext"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_ext.object', {
#             'object': obj
#         })


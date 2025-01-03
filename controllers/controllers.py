# -*- coding: utf-8 -*-
# from odoo import http


# class Hotel-ext(http.Controller):
#     @http.route('/hotel-ext/hotel-ext', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel-ext/hotel-ext/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel-ext.listing', {
#             'root': '/hotel-ext/hotel-ext',
#             'objects': http.request.env['hotel-ext.hotel-ext'].search([]),
#         })

#     @http.route('/hotel-ext/hotel-ext/objects/<model("hotel-ext.hotel-ext"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel-ext.object', {
#             'object': obj
#         })


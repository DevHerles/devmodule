# -*- coding: utf-8 -*-
from odoo import http

# class Devmodule(http.Controller):
#     @http.route('/devmodule/devmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/devmodule/devmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('devmodule.listing', {
#             'root': '/devmodule/devmodule',
#             'objects': http.request.env['devmodule.devmodule'].search([]),
#         })

#     @http.route('/devmodule/devmodule/objects/<model("devmodule.devmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('devmodule.object', {
#             'object': obj
#         })
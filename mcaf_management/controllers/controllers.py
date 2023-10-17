# -*- coding: utf-8 -*-
# from odoo import http


# class McafManagement(http.Controller):
#     @http.route('/mcaf_management/mcaf_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mcaf_management/mcaf_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mcaf_management.listing', {
#             'root': '/mcaf_management/mcaf_management',
#             'objects': http.request.env['mcaf_management.mcaf_management'].search([]),
#         })

#     @http.route('/mcaf_management/mcaf_management/objects/<model("mcaf_management.mcaf_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mcaf_management.object', {
#             'object': obj
#         })

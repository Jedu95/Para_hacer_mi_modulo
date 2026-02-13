# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloNuevo(http.Controller):
#     @http.route('/modulo_nuevo/modulo_nuevo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_nuevo/modulo_nuevo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_nuevo.listing', {
#             'root': '/modulo_nuevo/modulo_nuevo',
#             'objects': http.request.env['modulo_nuevo.modulo_nuevo'].search([]),
#         })

#     @http.route('/modulo_nuevo/modulo_nuevo/objects/<model("modulo_nuevo.modulo_nuevo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_nuevo.object', {
#             'object': obj
#         })

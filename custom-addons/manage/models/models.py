# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
     _name = 'nuevo_modulo.task'
     _description = 'datos de las tareas'

     name = fields.Char(string = 'nombre de la tarea')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odo
from odoo import api, fields, models


class semanas(models.Model):
    _name = 'asistencias.semanas'
    _description = 'NUMERO DE SEMANA'

    nombre_semana = fields.Char(string="Semana",)
    rango1 = fields.Date(string="Inicio",)
    rango2 = fields.Date(string="Fin",)
    semanas_ids = fields.Many2one(
        comodel_name='hr.attendance', string="Semanas")

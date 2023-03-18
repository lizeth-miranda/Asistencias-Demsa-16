# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models


class Account(models.Model):
    _inherit = 'account.analytic.account'

    resi = fields.Many2many('res.users', string='Residentes',)

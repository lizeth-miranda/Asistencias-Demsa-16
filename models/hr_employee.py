# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import fields, models, api, _


class empl(models.Model):
    _inherit = 'hr.employee'

    _sql_constraints = [
        ('pin_uniq', 'unique (num_employee)',
         "¡EL CÓDIGO DE EMPLEADO QUE SE INTENTA ASIGNAR YA EXISTE !"),
    ]

    ##Datos informativos y personales##
    num_employee = fields.Char(string="Número Empleado",
                               groups="hr.group_hr_user", tracking=True)

    fecha_ingreso = fields.Date(
        string="Fecha de Ingreso", groups="hr.group_hr_user", tracking=True)
    afiliacion_imss = fields.Char(
        string="Afiliación IMSS", groups="hr.group_hr_user", tracking=True)

    empresa = fields.Selection([
        ('enterprise', 'PCA Grupo Prefabricador'),
        ('enterprise2', 'DEMSA'),
        ('gba', 'GBA'),
    ], string="Empresa", groups="hr.group_hr_user", tracking=True)

    cate_emp = fields.Selection([
        ('admin', 'Administrativo'),
        ('planta', 'Planta'),
        ('obra', 'Obra'),
    ], string="Categoria Empleado", groups="hr.group_hr_user", tracking=True)

    user_resp = fields.Many2many(
        'res.users', string='Visualizar Asistencias', groups="hr.group_hr_user", tracking=True)

    ##COSTOS DEL EMPLEADO##
    salario = fields.Monetary(
        string="Salario Semanal", groups="hr.group_hr_user", tracking=True)
    cost_day = fields.Monetary(
        help="sueldo semanal/6", string="Costo/Día", compute="compute_costday", groups="hr.group_hr_user", tracking=True)

    costo_dayCS = fields.Monetary(
        string="Carga Social por Día", groups="hr.group_hr_user", tracking=True
    )

    timesheet_cost = fields.Monetary(
        'Costo por Hora', compute="compute_timecost", help="(sueldo/ 6) /8", groups="hr.group_hr_user", tracking=True)
    cost_extra = fields.Monetary(help="(sueldo/6) /8 *2", string="Costo Extra",
                                 compute="compute_costExtra", groups="hr.group_hr_user", tracking=True)
    cost_extra_bono = fields.Monetary(help="(sueldo + bono fijo/6) /8 *2)", string="Costo Extra + Bono",
                                      compute="compute_costExtra_bono", groups="hr.group_hr_user", tracking=True)
    cost_default = fields.Monetary(
        help="cost per absence", string="Costo/Falta", groups="hr.group_hr_user", tracking=True)
    cuenta = fields.Char('Cuenta De Depósito',
                         groups="hr.group_hr_user", tracking=True)
    clabe = fields.Char('CLABE Interbancaria',
                        groups="hr.group_hr_user", tracking=True)
    banco = fields.Many2one(comodel_name="res.bank", string="Banco",
                            groups="hr.group_hr_user", tracking=True)
    currency_id = fields.Many2one(
        comodel_name='res.currency',
    )
    credito_info = fields.Monetary(
        string="Crédito Infonavit", groups="hr.group_hr_user", tracking=True)
    credito_fona = fields.Monetary(
        string="Crédito Fonacot", groups="hr.group_hr_user", tracking=True)
    bono = fields.Monetary(
        string="Bono Fijo", groups="hr.group_hr_user", tracking=True)
    active_CEXB = fields.Boolean(
        string="Activar Costo Extra + Bono", groups="hr.group_hr_user", tracking=True)
    viati = fields.Monetary(
        string="Viáticos", groups="hr.group_hr_user", tracking=True)

    ##HORARIO LABORAL##
    horas_lab = fields.Float(string="Horas laborales",
                             groups="hr.group_hr_user", tracking=True)
    horas_lab_in = fields.Float(
        string="Horas Laborales CI", groups="hr.group_hr_user", tracking=True)
    hours = fields.Float(string="Horas Sábado",
                         groups="hr.group_hr_user", tracking=True)
    # normal = fields.Boolean(String="Horario normal",
    #                         groups="hr.group_hr_user", tracking=True)

    @api.depends('salario')
    def compute_costday(self):
        for rec in self:
            rec.cost_day = rec.salario/6

    @api.depends('salario')
    def compute_timecost(self):
        for rec in self:
            rec.timesheet_cost = (rec.salario/6) / 8

    @api.depends('salario')
    def compute_costExtra(self):
        for rec in self:
            r1 = (rec.salario/6)
            r2 = r1 / 8
            r3 = r2 * 2
            rec.cost_extra = r3

    @api.depends('salario')
    def compute_costExtra_bono(self):
        for rec in self:
            r4 = (rec.salario + rec.bono) / 6
            r5 = r4 / 8
            r6 = r5 * 2
            rec.cost_extra_bono = r6

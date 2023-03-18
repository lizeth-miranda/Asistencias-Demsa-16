# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models
#from datetime import date, datetime, timedelta
#from odoo.exceptions import ValidationError, UserError
# import time
# import pytz


class hr_atten(models.Model):
    _inherit = 'hr.attendance'

    account_ids = fields.Many2one(
        comodel_name='account.analytic.account',
        string="Proyecto",
    )
    account_ids_extras = fields.Many2one(
        comodel_name='account.analytic.account',
        string="Proyecto Tiempo Extra",
    )
    fecha = fields.Date(string="Fecha Registro",
                        required=True, readonly=False, default=fields.Date.context_today)
    Date = fields.Date(
        compute='compute_Date',
        store=True,)

    n_empleado = fields.Char(
        related="employee_id.num_employee",
        string="N° Empleado",
    )

    currency_id = fields.Many2one(
        related='employee_id.currency_id',
    )
   # cost_total = fields.Monetary(
    #     compute='compute_cost_total',
    #     store=True,
    #     string="Costo Total"
    # )
    hours_extra = fields.Float(
        compute='_hours_extra',
        string="Horas Extras",
        store=True,
    )

    hours = fields.Float(
        related="employee_id.horas_lab",
        string="Horas Laborales",
    )
    department = fields.Char(
        related="employee_id.department_id.name",
        string="Departamento",
    )
    manager = fields.Char(
        related="employee_id.parent_id.name", string="Responsable", store=True,)

    day = fields.Integer(
        compute='_day',
    )
    hours_sat = fields.Float(
        related="employee_id.hours",
    )
    # normal = fields.Boolean(
    #     related="employee_id.normal"
    # )
    total_hours = fields.Float(
        compute='_total_hours',
        # store=True,
        string="Horas Totales"
    )

    comen = fields.Char(string="Comentarios",)

    user_id = fields.Many2one('res.users', string='Residente',
                              required=False, readonly=True, default=lambda self: self.env.user.id)
    tipo_resid = fields.Selection(related="user_id.tipo_resi",)
    tipo_empl = fields.Selection(related="employee_id.cate_emp",)

    asistencia = fields.Boolean(default=True, string="asistencia",)

    block_lines = fields.Selection([('done', 'Registrado')], string='Estado', )
    #tem = fields.Float(string="Temperatura",)

    @ api.depends('Date')
    def _day(self):
        for record in self:
            record.day = record.Date.weekday()
    # fecha para agrupar las horas totales de los empleados con la fecha de la
    # asitencia y no la de la fecha registro

    @ api.depends('check_in')
    def compute_Date(self):
        for record in self:
            # dt = record.check_in
            # date = fields.Datetime.to_string(fields.Datetime.context_timestamp(
            #     self, fields.Datetime.from_string(dt)))[:10]
            # record.Date = date
            dt = fields.Date.from_string(record.check_in)
            record.Date = dt

    @ api.depends('Date')
    def _total_hours(self):
        for attendance in self:
            attendance.total_hours = sum(self.env['hr.attendance'].search([
                ('employee_id', '=', attendance.employee_id.name),
                # ('account_ids', '=', attendance.account_ids.id),
                ('Date', '=', attendance.Date),
            ]).mapped('worked_hours'))

    @ api.depends('worked_hours')
    def _hours_extra(self):
        for attendance in self:
            if attendance.day != 5 and attendance.total_hours >= attendance.hours and attendance.tipo_empl != 'admin':
                attendance.hours_extra = (
                    attendance.total_hours-attendance.hours)//1

            elif attendance.day == 5 and attendance.tipo_resid == 'planta' and attendance.tipo_empl != 'admin':
                attendance.hours_extra = attendance.total_hours

            elif attendance.day == 5 and attendance.tipo_resid == 'obra' and attendance.tipo_empl != 'admin':
                attendance.hours_extra = (
                    attendance.total_hours-attendance.hours_sat) // 1

            elif attendance.day == 6 and attendance.tipo_empl != 'admin':
                attendance.hours_extra = attendance.total_hours

    # @api.constrains('check_out')
    # def checks_out(self):
    #     for record in self:
    #         buscar = self.env['hr.attendance'].search_count([
    #             ('employee_id.id', '=', record.employee_id.id),
    #             ('worked_hours', '>', 24),
    #         ])
    #         if buscar > 0:
    #             raise exceptions.ValidationError(
    #                 # _("LA FECHA DE LA SALIDA DEBE SER IGUAL A LA FECHA DE ENTRADA, FAVOR DE REVISAR SUS DATOS"))
    #                 _("UN EMPLEADO NO PUEDE TRAJAR MAS DE 24 HRS, FAVOR DE REVISAR SUS DATOS"))
    # create a new line, as none existed before

    # @ api.constrains('Date')
    # def nomina_line(self):
    #     for record in self:
    #         nomina_line = self.env['nomina.line'].search_count([
    #             ('employee_id.id', '=', record.employee_id.id),
    #             ('project', '=', record.account_ids.id),
    #             ('fechaA', '=', record.Date),
    #             ('check_in', '=', record.check_in),
    #             ('check_out', '=', record.check_out),
    #         ])
    #         print(nomina_line)
    #         if nomina_line > 0:
    #             raise ValidationError(
    #                 _("Una o varias asistencias ya existen registradas "))

    #         elif not nomina_line:
    #             record.env['nomina.line'].create({
    #                 'employee_id': record.employee_id.id,
    #                 'department': record.department,
    #                 'project': record.account_ids.id,
    #                 'fechaA': record.Date,
    #                 'check_in': record.check_in,
    #                 'check_out': record.check_out,
    #                 'worked_hours': record.worked_hours,
    #                 'notas': record.comen,
    #                 'us_id': record.user_id.name,
    #                 'type_resi': record.tipo_resid,
    #                 'asis': record.asistencia,
    #                 # 'total_extra': record.total_extra,
    #                 # 'cost_total': record.cost_total,
    #                 # 'total_inci': record.total_inci,

    #             })
    #             record.block_lines = 'done'
    #     return {
    #         'effect': {
    #             'fadeout': 'slow',
    #             'message': 'Registro Exitoso',
    #             'type': 'rainbow_man',
    #         }
    #     }

     #   }

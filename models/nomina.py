# -*- coding: utf-8 -*-
# instruccion para hacer importaciones desde odoo
from odoo import api, fields, models, exceptions, _
# from datetime import date, datetime, timedelta
# from odoo.exceptions import ValidationError, UserError


class Nomina(models.Model):
    _name = 'nomina.demsa'
    _description = 'Registro de Nomina'

    # active = fields.Boolean(string="Archivado", default=True,)
    # us_id = fields.Char(string="Residente",)
    # type_resi = fields.Char(string="Tipo",)

    employee_name = fields.Many2one(
        comodel_name='hr.employee', string="Empleado", )

    # attendance_line = fields.One2many(
    #     'hr.attendance', 'attendance_id', string="Datos Asistencia",)
    # semanas_line = fields.One2many(
    #     'asistencias.semanas', 'semanas_ids', string="Semanas Asistencias")
    # semana = fields.Char("Numero de Semana",
    #                      compute="compute_num_semana", store=True,)

    name = fields.Char(string="name",)
    date_from = fields.Date(
        string='From',  required=True,
    )
    date_to = fields.Date(
        string='To',  required=True,
    )
    # num_asis = fields.Float(related="attendance_ids.employee_id.num_asistencias",
    #                         string="Total Asistencias", )
    #num_inci = fields.Float(string="Total Incidencias",)
    currency_id = fields.Many2one(
        related='employee_name.currency_id',
    )

    # metodo que obtiene la secuencia
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('nomina.demsa')
        return super(Nomina, self).create(vals)

    #  # metodo que obtiene el numero de semana
    # @api.depends('employee_name')
    # def compute_num_semana(self):
    #     for record in self:
    #         cadena = self.env['asistencias.semanas'].search([
    #             ('rango1', '<=', record.date_from),
    #             ('rango2', '>=', record.date_to),
    #         ]).mapped('nombre_semana')

    #         record.semana = ''.join(map(str, (cadena)))

    # employee_id = fields.Many2one(
    #     comodel_name='hr.employee',
    #     string="Trabajador",
    #     readonly=True,
    # )
    # department = fields.Char(
    #     string="Departamento",
    #     readonly=True,
    # )
    # empre = fields.Selection(related="employee_id.empresa", string="Empresa")
    # project = fields.Many2one(
    #     comodel_name='account.analytic.account',
    #     string="Obra",
    #     readonly=True,
    # )
    # puesto_trabajo = fields.Many2one(
    #     related="employee_id.department_id",
    #     string="Puesto",
    # )
    # codigo_empleado = fields.Char(
    #     related="employee_id.codigo",
    #     string="# empleado",
    # )
    # sueldo_semanal = fields.Monetary(
    #     related="employee_id.salario",
    #     string="Sueldo Semanal",
    #     readonly=True,
    # )
    # cost_day = fields.Monetary(
    #     help="sueldo semanal/6",
    #     related="employee_id.cost_day",
    #     string="Costo/Día",
    #     readonly=True,
    # )
    # cost_hour = fields.Monetary(
    #     help="Costo por día/8",
    #     related="employee_id.timesheet_cost",
    #     string="Costo/Hora",
    #     readonly=True,
    # )
    # extra_cost = fields.Monetary(
    #     help="sueldo semanal/6/8*2",
    #     related="employee_id.cost_extra",
    #     string="Costo Extra/hr",
    #     readonly=True,
    # )
    # costo_extra_bono = fields.Monetary(
    #     help="(((sueldo semanal + Bono fijo) /6)/8)*2",
    #     related="employee_id.cost_extra_bono",
    #     string="Costo Extra/hr + Bono",
    #     readonly=True,
    # )
    # cost_default = fields.Monetary(
    #     help="Costo por día + carga social",
    #     related='employee_id.cost_default',
    #     string="Costo/Falta",
    # )
    # hours = fields.Float(
    #     related="employee_id.horas_lab",
    #     string="Horas laborales",
    # )

    # day = fields.Integer(
    #     compute='_day',
    # )
    # normal = fields.Boolean(
    #     related="employee_id.normal",
    #     string="Horario Normal",
    # )
    # # mitad = fields.Float(
    # #     compute="_mitad"
    # # )
    # hours_sat = fields.Float(
    #     related="employee_id.hours",
    #     string="Horas laborales sábados",
    # )
    # hrs_lab_in = fields.Float(related="employee_id.horas_lab_in",)
    # # Date = fields.Date(
    # #     compute='_Date',
    # #     store=True,
    # # )
    # nomina_date = fields.Date(
    #     default=fields.Date.context_today,
    # )
    # notas = fields.Text(
    #     string="Notas",
    # )

    # worked_hours = fields.Float(
    #     help="Horales laborales + horas extras",
    #     string="Horas Trabajadas",
    #     compute='_compute_worked_hours',
    #     store=True,
    # )
    # hours_extra = fields.Float(
    #     help="horas trabajadas - horas laborales",
    #     string="Horas Extras",
    #     compute='_hours_extra',
    #     inverse='_inverse_hours_extra',
    #     store=True,
    # )
    # total_extra = fields.Monetary(
    #     help="Horas extras * Costo/ hora extra",
    #     string="Total Extra",
    #     compute='compute_total_extra',
    #     store=False,
    #     readonly=True,
    # )
    # total_inci = fields.Monetary(string="Total Incidencia")
    # cost_total = fields.Monetary(
    #     help="costo/ día + total extra",
    #     compute='compute_cost_total',
    #     store=True,
    #     readonly=True,
    #     string="Costo total/Día",
    # )
    # currency_id = fields.Many2one(
    #     related='employee_id.currency_id',
    # )

    # # total_hours = fields.Float(
    # #     compute='_total_hours',
    # #     # store=True,
    # # )
    # state = fields.Selection([
    #     ('draft', 'Borrador'),
    #     ('confirm', 'Confirmado'),
    # ], string='Status', readonly=True, default='draft', store=True,)

    # responsible_id = fields.Many2one(
    #     comodel_name='res.users',
    #     ondelete='set null',
    #     index=True,
    # )
    # inci = fields.Char(string="Incidencia",)
    # leavee = fields.Boolean(string="Falta",)
    # fecha_ing = fields.Date(related="employee_id.fecha_ingreso",)
    # nuevo_ing = fields.Boolean(
    #     string="Nuevo Ingreso, Descuentos",
    #     help="la casilla se marcacuando el sueldo a pagar es por nuevo ingreso u otros casos similares")
    # # cuentas bancarias
    # account = fields.Char(related="employee_id.cuenta",
    #                       string="Cuenta de depósito",)
    # cla = fields.Char(related="employee_id.clabe",
    #                   string="CLABE Interbancaria",)
    # bank = fields.Many2one(related="employee_id.banco", string="Banco",)
    # # PERCEPCIONES

    # viat = fields.Monetary(
    #     related="employee_id.viati",
    #     string="Viáticos"
    # )
    # pasa = fields.Monetary(
    #     string="Pasaje",
    # )
    # bono = fields.Monetary(
    #     related="employee_id.bono",
    #     string="Bono Fijo",
    # )
    # bono_even = fields.Monetary(
    #     string="Bono Eventual",
    # )
    # gasolina = fields.Monetary(
    #     string="Gasolina",
    # )
    # vacaciones = fields.Monetary(
    #     string="Vacaciones",
    # )
    # prima_vaca = fields.Monetary(
    #     string="Prima Vacacional",
    # )
    # aguin = fields.Monetary(
    #     string="Aguinaldo",
    # )
    # costo_daycs = fields.Monetary(
    #     related="employee_id.costo_dayCS",
    # )
    # suma_percep = fields.Monetary(
    #     help="costo/día + total extra + carga social",
    #     compute="sum_perc",
    #     string="Costo MO",
    #     store=True
    # )
    # sum_perc_notCarga = fields.Monetary(
    #     compute="compute_sum_perc_noCS", string="Suma Percepciones", store=True)

    # semana_fondo = fields.Monetary(string="Semana de Fondo",)

    # pres_personal = fields.Monetary(
    #     string="Deposito Préstamo Personal", related="employee_id.depo")
    # others = fields.Monetary(string="Reembolsos u otros",)

    # # Deducciones
    # cre_info = fields.Monetary(
    #     related="employee_id.credito_info",
    #     string="Crédito Infonavit"
    # )
    # fona = fields.Monetary(
    #     related="employee_id.credito_fona",
    #     string="Crédito Fonacot",
    # )
    # pres_per = fields.Monetary(
    #     string="Préstamo Personal", related="employee_id.pres_perso",)

    # des_epp = fields.Monetary(
    #     string="Desc. EPP Herramienta", related="employee_id.desc_HPP",)
    # otros_desc = fields.Monetary(
    #     string="Otros Descuentos", related="employee_id.otros_desc",)

    # sueldo_pagar = fields.Monetary(
    #     help="(Sueldo semanal + Suma percepciones + suma hrs extras) - deducciones ",
    #     string="Sueldo a pagar",
    #     compute="suel_pagar",
    #     store=True,
    # )

    # suma_dedu = fields.Monetary(
    #     string="Suma Deducciones",
    #     compute="sum_dedu",
    #     store=True
    # )

    # otros = fields.Monetary(string="Otros",)
    # # Costo semanal
    # reg_sem = fields.Selection([('week', 'Semanal')], string='Tipo Registro', )

    # horas_extras_sem = fields.Monetary(
    #     compute='hrs_ex_sem', string='Suma Costo Hrs Extras', store=True,)
    # sum_horas_extras = fields.Float(
    #     compute='compute_sumHE', string="Suma Horas Extras", store=True)

    # # calcular costo/dia en una falta
    # costo_falta = fields.Monetary(compute="compute_costo_falta", store=True,)

    # # suma_costoMO = fields.Monetary(
    # #     compute="compute_sumaMO", string="Costo MO Semanal", store=True,)

    # nomina = fields.Boolean(default=True, string="nomina",)
    # asis = fields.Boolean(string="Asistencia",)
    # active_CEXB2 = fields.Boolean(
    #     string="Costo Extra + Bono Fijo", related="employee_id.active_CEXB",)
    # test_date = fields.Date(string="Date test",)

    # # metodo que suma las horas extras semanales
    # @api.depends('reg_sem')
    # def compute_sumHE(self):
    #     for record in self:
    #         record.sum_horas_extras = sum(self.env['nomina.line'].search([
    #             ('semana', '=', record.semana),
    #             ('employee_id', '=', record.employee_id.id),
    #             #('reg_sem', 'in', ['week', 'semanal'])
    #         ]).mapped('hours_extra'))

    # # metodo que obtiene el numero de semana
    # @api.depends('fechaA')
    # def compute_num_semana(self):
    #     for record in self:
    #         cadena = self.env['semanas.nomina'].search([
    #             ('rango1', '<=', record.fechaA),
    #             ('rango2', '>=', record.fechaA),
    #         ]).mapped('nombre_semana')

    #         record.semana = ''.join(map(str, (cadena)))

    # # suma el costo extra semanal

    # @ api.depends('reg_sem')
    # def hrs_ex_sem(self):
    #     for record in self:
    #         record.horas_extras_sem = sum(self.env['nomina.line'].search([
    #             ('semana', '=', record.semana),
    #             ('employee_id', '=', record.employee_id.id),
    #             # ('reg_sem', 'in', ['week', 'semanal'])
    #         ]).mapped('total_extra'))

    # # obtiene el numero de dia de la fecha de asistencia
    # @ api.depends('fechaA')
    # def _day(self):
    #     for record in self:
    #         record.day = record.fechaA.weekday()

    # # calcula las horas trabajas
    # @ api.depends('check_in', 'check_out')
    # def _compute_worked_hours(self):
    #     for rec in self:
    #         if rec.check_out:
    #             delta = rec.check_out-rec.check_in
    #             rec.worked_hours = delta.total_seconds() / 3600.0
    #         else:
    #             rec.worked_hours = False
    # # metodo que permite volver un campo calculado editable

    # @ api.depends('worked_hours')
    # def _inverse_hours_extra(self):
    #     for record in self:
    #         record.hours_extra = record.hours_extra + 0

    # # obtiene las horas extras, dependiendo del tipo de empleado y el dia laborado
    # @ api.depends('worked_hours')
    # def _hours_extra(self):
    #     for record in self:
    #         if record.day != 5 and record.worked_hours >= record.hours:
    #             record.hours_extra = (record.worked_hours-record.hours) // 1

    #         elif record.day == 5 and record.type_resi == 'planta':
    #             record.hours_extra = record.worked_hours

    #         elif record.day == 5 and record.type_resi == 'obra':
    #             record.hours_extra = (
    #                 record.worked_hours-record.hours_sat) // 1

    #         elif record.day == 6:
    #             record.hours_extra = record.worked_hours

    # # metodo para añadirle un bono extra en el calculo de la nomina

    # @ api.depends('active_CEXB2')
    # def compute_total_extra(self):
    #     for record in self:
    #         if record.active_CEXB2 == True:
    #             record.total_extra = (
    #                 record.hours_extra * record.costo_extra_bono)
    #         elif record.active_CEXB2 == False:
    #             record.total_extra = (record.hours_extra * record.extra_cost)

    # # metodo que obtiene el costo por dia, donde se incluyte el costo extra
    # @ api.depends('hrs_lab_in', 'hours_extra')
    # def compute_cost_total(self):
    #     for record in self:
    #         if record.day != 5:
    #             # t0 = record.worked_hours-record.hours_extra
    #             t1 = (record.hrs_lab_in * record.cost_hour)
    #             record.cost_total = (t1 + record.total_extra)

    #         elif record.day == 5 and record.type_resi == 'obra':
    #             t1 = (record.hrs_lab_in * record.cost_hour)
    #             record.cost_total = t1 + record.total_extra

    #         elif record.day == 5 and record.type_resi == 'planta':
    #             record.cost_total = record.total_extra

    #         elif record.day == 6:
    #             record.cost_total = record.total_extra

    # @ api.depends('leavee')
    # def compute_costo_falta(self):
    #     for rec in self:
    #         if rec.leavee == True:
    #             rec.cost_total = rec.cost_default

    #  # calculo sueldo a pagar
    # # calculo del costo de obra con la carga social

    # @ api.depends('cost_total', 'viat', 'bono', 'pasa', 'bono_even', 'gasolina', 'vacaciones', 'aguin')
    # def sum_perc(self):
    #     for record in self:
    #         if record.inci != False:
    #             record.suma_percep = (record.cost_total + record.viat + record.pasa + record.bono +
    #                                   record.bono_even + record.gasolina +
    #                                   record.vacaciones + record.prima_vaca + record.aguin) * -1
    #         else:
    #             record.suma_percep = (record.cost_total + record.viat + record.pasa + record.bono +
    #                                   record.bono_even + record.gasolina +
    #                                   record.vacaciones + record.prima_vaca + record.aguin + record.costo_daycs) * -1
    # # calcular las faltas y asistencias
    # cant_ausen = fields.Float(
    #     compute="compute_cant_ausen", string="Cantidad de Ausencias",)
    # cant_asis = fields.Float(compute="compute_cant_asis",
    #                          string="Cantidad de Asistencias",)
    # cant_reg_Sem = fields.Float(compute="compute_cant_reg_Sem",
    #                             string="Cantidad de rgistri",)

    # # obtiene la cantidad de ausencias
    # @ api.depends('reg_sem')
    # def compute_cant_ausen(self):
    #     for record in self:
    #         record.cant_ausen = self.env['nomina.line'].search_count([
    #             ('semana', '=', record.semana),
    #             ('employee_id', '=', record.employee_id.id),
    #             # ('reg_sem', 'in', ['week', 'semanal'])
    #             ('leavee', '=', True),
    #         ])

    # # obtiene la cantidad de asistencias
    # @ api.depends('reg_sem')
    # def compute_cant_asis(self):
    #     for record in self:
    #         record.cant_asis = self.env['nomina.line'].search_count([
    #             ('semana', '=', record.semana),
    #             # ('reg_sem', 'in', ['week', 'semanal'])
    #             ('employee_id', '=', record.employee_id.id),
    #             ('asis', '=', True),
    #         ])
    # suel_Sem_faltas = fields.Monetary(
    #     compute="compute_suel_sem_faltas", string="Sueldo semanal con faltas",)

    # # obtiene el costo por falta
    # @ api.depends('cant_asis', 'cant_ausen')
    # def compute_suel_sem_faltas(self):
    #     # for rec in self:
    #     #     m1 = rec.cant_asis + rec.cant_ausen
    #     #     if m1 < 6:
    #     #         rec.suel_Sem_faltas = (
    #     #             rec.cost_day * rec.cant_asis + rec.cost_day) - (rec.extra_cost * rec.cant_ausen)
    #     #     else:
    #     #         rec.suel_Sem_faltas = (
    #     #             rec.cost_day * rec.cant_asis) - (rec.extra_cost * rec.cant_ausen)

    #     for rec in self:
    #         busqueda = self.env['nomina.line'].search_count([
    #             ('semana', '=', rec.semana),
    #             # ('reg_sem', 'in', ['week', 'semanal'])
    #             ('employee_id', '=', rec.employee_id.id),
    #             ('inci', '=', "INCAPACIDAD"),
    #         ])

    #         if busqueda > 1 or rec.cant_asis >= 5:
    #             rec.suel_Sem_faltas = (
    #                 rec.cost_day * rec.cant_asis) - (rec.extra_cost * rec.cant_ausen)
    #         else:
    #             rec.suel_Sem_faltas = (
    #                 rec.cost_day * rec.cant_asis + rec.cost_day) - (rec.extra_cost * rec.cant_ausen)

    # suel_nuevo_ingreso = fields.Monetary(
    #     compute="compute_suel_nuevo_ingreso", string="Sueldo Nuevo Ingreso",)

    # @ api.depends('cost_day', 'cant_asis')
    # def compute_suel_nuevo_ingreso(self):
    #     for rec in self:
    #         rec.suel_nuevo_ingreso = rec.cost_day * rec.cant_asis

    # # calculo costo de percepciones sin carga social para la nómina

    # @ api.depends('reg_sem')
    # def compute_sum_perc_noCS(self):
    #     for record in self:
    #         if record.reg_sem in ['week', 'semanal'] and record.cant_asis >= 5 and record.cant_ausen == 0 and record.nuevo_ing == False:
    #             record.sum_perc_notCarga = (record.sueldo_semanal + record.viat + record.pasa + record.bono +
    #                                         record.bono_even + record.gasolina +
    #                                         record.vacaciones + record.prima_vaca + record.aguin + record.semana_fondo + record.pres_personal + record.others)

    #         elif record.reg_sem in ['week', 'semanal'] and record.cant_asis < 6 and record.cant_ausen > 0 and record.nuevo_ing == False:
    #             record.sum_perc_notCarga = (record.suel_Sem_faltas + record.viat + record.pasa + record.bono +
    #                                         record.bono_even + record.gasolina +
    #                                         record.vacaciones + record.prima_vaca + record.aguin + record.semana_fondo + record.pres_personal + record.others)

    #         elif record.reg_sem in ['week', 'semanal'] and record.nuevo_ing == True:
    #             record.sum_perc_notCarga = (record.suel_nuevo_ingreso + record.viat + record.pasa + record.bono +
    #                                         record.bono_even + record.gasolina +
    #                                         record.vacaciones + record.prima_vaca + record.aguin + record.semana_fondo + record.pres_personal + record.others)

    # @ api.depends('reg_sem')
    # def sum_dedu(self):
    #     for record in self:
    #         if record.reg_sem in ['week', 'semanal']:
    #             record.suma_dedu = record.cre_info + record.fona + \
    #                 record.pres_per + record.des_epp + record.otros_desc + record.otros

    # @ api.depends('reg_sem')
    # def suel_pagar(self):
    #     for record in self:
    #         if record.reg_sem in ['week', 'semanal']:
    #             record.sueldo_pagar = (
    #                 record.sum_perc_notCarga + record.horas_extras_sem) - record.suma_dedu
    #         elif record.reg_sem not in ['week', 'semanal']:
    #             record.sueldo_pagar = False

    # # create a new line, as none existed before

    # @ api.constrains('date', 'name', 'amount')
    # def acco_line(self):
    #     for record in self:
    #         record.state = 'confirm'
    #         account_line = self.env['account.analytic.line'].search_count([
    #             ('date', '=', record.fechaA),
    #             ('name', '=', record.employee_id.name),
    #             ('job_pos', '=', record.department),
    #             ('account_id', '=', record.project.id),
    #             ('amount', '=', record.suma_percep),
    #         ])
    #         if account_line > 0:
    #             raise ValidationError(
    #                 _("Uno o varios de los registros ya fueron Confirmados"))

    #         elif not account_line:
    #             self.env['account.analytic.line'].create({
    #                 'date': record.fechaA,
    #                 'name': record.employee_id.name,
    #                 'nom': record.nomina,
    #                 'job_pos': record.department,
    #                 'account_id': record.project.id,
    #                 'amount': record.suma_percep,
    #             })
    #     return {
    #         'effect': {
    #             'fadeout': 'slow',
    #             'message': 'Registro Exitoso',
    #             'type': 'rainbow_man',
    #         }
    #     }

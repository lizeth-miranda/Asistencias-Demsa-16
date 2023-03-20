# -*- coding: utf-8 -*-
{
    'name': 'Asistencias Demsa16',
    'version': '16.0',
    'author': 'Demsa Industrial',
    'website': '',
    'depends': [
        'hr',
        'hr_attendance',
        # 'account',
        # 'account_accountant',
        # 'asistencias.semanas',
        # 'hr_timesheet',
        # 'hr_holidays',
        # 'sale_management',
        # 'purchase',
        # 'nomina.line'
    ],
    'data': [
        # security
        # 'security/ir.model.access.csv',
        # 'security/semanas_group.xml',
        # 'security/nomina_user_group.xml',
        # 'security/nomina_group.xml',

        # data
        # 'data/sequence.xml',
        # wizards
        # reports
        # demo
        # views
        'views/hr_attendance.xml',
        'views/hr_employee.xml',
        # 'views/account_analytic.xml',
        'views/account_analytic_account.xml',
        'views/res_user.xml',
        # 'views/visor_asistencias_planta.xml',
        'views/groups_acuerdocompra_basico.xml',
        'views/groups_asistencias_planta.xml',
        'views/groups_controlobra.xml',
        'views/groups_empleado_usuario.xml',

        # 'views/semanas.xml',
        # 'views/nomina.xml',
        # 'views/hr_leave.xml',
    ],
    'license': 'LGPL-3',
}

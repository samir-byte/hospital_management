# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PatientCardReport(models.AbstractModel):
    _name = 'report.hospital_management.report_patient'

    @api.model
    def _get_report_values(self,docids,data=None):
        docs= self.env['hospital.patient'].browse(docids[0])
        appointments= self.env['hospital.appointment'].search([])
        for app in appointments:
            appointment_lists=[]
            vals={
                'name':app.name,
                'note':app.note,
                'date':app.date,
            }
            appointment_lists.append(vals)
        return{
            'doc_ids': docids,
            'doc_model': 'hospital.patient',
            'data': data,
            'docs': docs,
            'appointment_list': appointment_lists
        }
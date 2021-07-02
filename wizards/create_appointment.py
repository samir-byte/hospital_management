# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    name = fields.Many2one('hospital.patient', string='Patient')
    date = fields.Date(string='Appointment Date')

    def create_appointmen(self):
        vals={
            'name':self.name,
            'date':self.date
        }
        self.env['create.appointment'].create(vals)

    def get_appointments(self):
        appointments = self.env['hospital.appointment'].search_count([])
        print("get data")
        print(appointments)

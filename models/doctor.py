from odoo import models, fields, api

class Doctor(models.Model):
    _name = 'hospital.doctor'

    doctor_id = fields.Integer(string='Doctor Id')
    name = fields.Char(string='Name')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'),('female', 'Female')])

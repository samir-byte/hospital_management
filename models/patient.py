from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"
    # _rec_name = "patient_name"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', track_visibility='onchange')
    gender = fields.Selection([
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ], required=True, default='male')
    note = fields.Text(string='Registration Notes')
    image = fields.Binary(string='Image')
    # seq_num= fields.Char(string='Order Reference', required=True, copy=False, readonly=True)
    age_grp = fields.Selection(string='Age Group', selection=[('major', 'Major'),('minor', 'Minor')], compute='set_age_grp')
    appointment_count = fields.Integer(string='Appointment', compute='_get_appointment_count')
    def set_age_grp(self):
        for record in self:
            if record.age < 18:
                record.age_grp = 'minor'
            else:
                record.age_grp = 'major'

        return record.age_grp

    @api.constrains('age')
    def _check_age(self):
        # CODE HERE
        for rec in self:
            if rec.age <= 5:
                raise ValidationError('age must be greater than ')
    
    def open_patient_appointments(self):
        return {
            'name': 'Appointment',
            'domain': [('name','=', self.name)],
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def _get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('name','=',self.name)])
        return self.appointment_count
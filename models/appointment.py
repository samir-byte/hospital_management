from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"
    _order = "id desc"
    _rec_name = "name"

    def action_confirm(self):
        for record in self:
            record.state = 'confirm'
        return record.state

    def action_done(self):
        for record in self:
            record.state = 'done'
        return record.state

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
        return record.state


    name = fields.Many2one('hospital.patient', string='Patient')
    age = fields.Integer(string='Age', track_visibility='onchange', related='name.age')
    gender = fields.Selection([
        ('male','male'),
        ('female','female'),
        ('other','other'),
    ], required=True, default='male')
    date = fields.Date(string='Date')
    note = fields.Text(string='Registration Notes')
    state = fields.Selection(string='Status',readonly=True, default='draft', selection=[('draft', 'Draft'),('confirm','Confirm'),('done','Done'),('cancel','Cancelled')])


    
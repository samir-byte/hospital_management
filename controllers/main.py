from odoo import http
from odoo.http import request

class Hospital(http.Controller):
    #sample controller created
    @http.route('/hospital/patient/',website = True, auth='public')
    def hospital_patient(self, **kw):
        # return "hello world"
        patients = request.env['hospital.patient'].sudo().search([])
        return request.render("hospital_management.patients_page",{
            'patients': patients,
        })

class Hospital(http.Controller):

    @http.route('/patient_webform',type="http", auth="public", website=True)
    def patient_webform(self, **kw):
        return http.request.render('hospital_management.create_patient',{})

    @http.route('/create/webpatient', type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        request.env['hospital.patient'].sudo().create(kw)
        return request.render("hospital_management.patient_thanks",{})
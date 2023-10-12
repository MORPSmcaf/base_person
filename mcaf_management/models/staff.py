from odoo import models, fields, api


class MacfStaff(models.Model):
    _name = 'mcaf.management.staff'
    _description = 'Mcaf Staff'
    _inherit = 'mcaf.management.person'

    staff_id = fields.Char(string='Staff ID', required=True)
    d_o_b = fields.Date(string='Date of Birth')
    mail = fields.Text(string='Email Address')
    address = fields.Text(string = 'Physical Address')
    department = fields.Text(string='Department of working')

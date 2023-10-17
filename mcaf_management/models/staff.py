from odoo import models, fields, api


class McafStaff(models.TransientModel):
    _name = 'mcaf.management.staff'
    _description = 'Mcaf Staff'
    _inherit = 'mcaf.management.person'

    staff_id = fields.Char(string='Staff ID', required=True)
    d_o_b = fields.Date(string='Date of Birth')
    mail = fields.Text(string='Email Address')
    address = fields.Text(string = 'Physical Address')
    department = fields.Text(string='Department of working')

    def add_staff_member(self):
        # Create a new staff member in the 'mcaf.management.staff' model
        staff_model = self.env['mcaf.management.staff']
        staff_model.create({
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'staff_id': self.staff_id,
            'd_o_b': self.d_o_b,
            'mail': self.mail,
            'address': self.address,
            'department': self.department,
        })
        return {'type': 'ir.actions.act_window_close'}

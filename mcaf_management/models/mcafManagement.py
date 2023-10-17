from odoo import models, fields, api


class McafManagement(models.Model):
    _name = 'mcaf.management'
    _description = 'mcaf management'

    location_1 = fields.Char(string='Location 1')
    location_2 = fields.Char(string='Location 2')

    # person_id = fields.One2many(comodel_name='mcaf.management.person', inverse_name='person_id', string='People')

    def action_open_add_staff_wizard(self):
        return {
            'name': 'Mcaf Staff Member',
            'type': 'ir.actions.act_window',
            'res_model': 'mcaf.management.staff',
            'view_mode': 'form',
            'view_id': False,
            'target': 'new',
        }



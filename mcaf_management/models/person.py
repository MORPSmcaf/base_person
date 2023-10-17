from odoo import models, fields


class Person(models.Model):
    _name = 'mcaf.management.person'
    _description = 'Mcaf Person'
    _inherit = 'mcaf.management'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')],
        string='Gender')
    # person_id = fields.Integer(string='ID')
    # person_ids = fields.Many2one(comodel_name='mcaf.management', string='Mcaf Management')


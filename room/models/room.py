from odoo import models, fields


class RoomType(models.Model):
    _name = 'room.type'
    _description = 'Room Type'

    name = fields.Char(string='Type', required=True)
    description = fields.Text(string='Description')


class ActivityType(models.Model):
    _name = 'room.activity'
    _description = 'Activity Type'

    name = fields.Char(string='Type', required=True)
    description = fields.Text(string='Description')


class ShowActivity(models.Model):
    _name = 'room.show.activity'
    _description = 'Show Activity'
    # _inherit = 'room.reservation'

    activity_type_id = fields.Many2one('room.activity', string='Activity Type', required=True)
    activity_summary = fields.Text(string="Summary", required=True)
    activity_assigned = fields.Many2one('res.partner', string="Assigned To", required=True)
    activity_dueDate = fields.Date(string="Activity Due Date", required=True)


    def show_activity(self):
        # Create a new staff member in the 'mcaf.management.staff' model
        staff_model = self.env['room.show.activity']
        staff_model.create({
            'activity_summary': self.activity_summary,
            'activity_assigned': self.activity_assigned,
            'activity_dueDate': self.activity_dueDate,

        })
        return {'type': 'ir.actions.act_window_close'}







class RoomReservation(models.Model):
    _name = 'room.reservation'
    _description = 'Room Reservation'

    name = fields.Char(string='Display Name', required=True)
    room_type_id = fields.Many2one('room.type', string='Resource', required=True)
    reservation_des = fields.Text(string='Reservation Description')
    check_in_date = fields.Date(string='Start Date & Time', required=True)
    check_out_date = fields.Date(string='End Date & Time', required=True)
    seats = fields.Integer(string='Seats')


    def action_show_activity(self):
        return {
            'name': 'Show Activity',
            'type': 'ir.actions.act_window',
            'res_model': 'room.show.activity',
            'view_mode': 'form',
            'view_id': False,
            'target': 'new',
        }

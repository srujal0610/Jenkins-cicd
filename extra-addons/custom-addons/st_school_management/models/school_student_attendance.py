from odoo import fields, models
from odoo.exceptions import UserError

class SchoolStudentAttendance(models.Model):
    _name = 'school.student.attendance'

    student_id=fields.Many2one(comodel_name='school.student')
    attendance_id=fields.Float(related="student_id.attendance", store=True)

    def send_attendance(self):
        name =self.env['school.student'].search([('name','=','Kushal Shah')])
        print(name.attendance)

    # def send_reminder(self):

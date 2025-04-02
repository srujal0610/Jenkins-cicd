from odoo import models,fields

class SchoolSports(models.Model):
    _name = 'school.sports'

    name=fields.Char(string="Sport Name")
    students_ids=fields.Many2many(comodel_name='school.student',relation='school_student_sports_rel',column1='sport_id',column2='student_id', string="Students")
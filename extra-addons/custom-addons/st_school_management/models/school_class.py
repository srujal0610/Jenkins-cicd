from odoo import fields, models

class Classroom(models.Model):
    _name = 'school.class'
    _rec_name = 'grade'

    name=fields.Char(string="Class")
    grade=fields.Char(string="grade")
    student_ids = fields.One2many(comodel_name='school.student', inverse_name='class_id', string="Students")
    teacher_id = fields.Many2one(comodel_name='school.teacher', string='Class Teacher')
    subject_ids=fields.Many2many(comodel_name='school.subjects', relation='class_subject_rel', column1='class_id',
                                 column2='subject_id', string='Subjects')


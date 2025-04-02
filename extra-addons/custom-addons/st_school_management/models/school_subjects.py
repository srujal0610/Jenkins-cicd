from odoo import fields, models


class SchoolSubjects(models.Model):
    _name = 'school.subjects'
    _rec_name = 'name'

    name=fields.Char(string='Subject Name')
    student_id=fields.Many2many(comodel_name='school.student', relation='subject_student_rel', column1='subject_id', column2='student_id', string="Student")
    teacher_ids=fields.One2many(comodel_name='school.teacher', string='Teacher', inverse_name='subject_id')
    grade_ids=fields.Many2many(comodel_name='school.class', relation='class_subject_rel', column1='subject_id', column2='class_id', string='Classes')
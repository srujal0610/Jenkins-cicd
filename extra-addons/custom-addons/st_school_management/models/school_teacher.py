from odoo import models, fields


class Teacher(models.Model):
    _name = 'school.teacher'
    _inherit = 'school.common'
    _description = 'Model for Teachers'

    user_id = fields.Many2one(comodel_name='res.users', string='Assigned User')
    subject_id=fields.Many2one(comodel_name='school.subjects', string="Subject")
    class_ids = fields.One2many(comodel_name='school.class', inverse_name='teacher_id', string="Assigned Classes")

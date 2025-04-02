from odoo import fields, models

class ResUsers(models.Model):
    _inherit='res.users'

    teacher_class_id=fields.Many2one(comodel_name='school.class', string="Assigned Class")
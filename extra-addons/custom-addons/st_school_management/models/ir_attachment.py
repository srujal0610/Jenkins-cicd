from odoo import models,fields

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    student_id = fields.Many2one(comodel_name='school.student')
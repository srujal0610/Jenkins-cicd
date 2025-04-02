from odoo import fields, models

class ChangeDobWizard(models.TransientModel):
    _name = 'school.student.dob.wizard'
    _description = 'Change Student DOB Wizard'

    new_dob = fields.Date(string='New Date of Birth', required=True)

    student_id = fields.Many2one(comodel_name='school.student', string='Student', required=True)

    def change_dob(self):
        for wizard in self:
            if wizard.new_dob:
                wizard.student_id.dob = wizard.new_dob

        return {'type': 'ir.actions.act_window_close'}

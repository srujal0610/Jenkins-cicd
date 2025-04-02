from odoo import fields, models,api

class StudentReports(models.Model):
    _name = 'school.student.reports'
    _rec_name = 'student_id'

    student_id=fields.Many2one(comodel_name='school.student', string="Student")
    maths_marks=fields.Float(string="Maths")
    maths_total_marks=fields.Float(string="Out of", default=1)
    chemistry_marks = fields.Float(string="Chemistry")
    chemistry_total_marks = fields.Float(string="Out of")
    physics_marks=fields.Float(string="Physics")
    physics_total_marks = fields.Float(string="Out of")

    total_marks=fields.Float(string="Total", compute="_compute_total")
    percentage=fields.Float(string="Percentage", compute="_compute_percentage", default=1)

    @api.depends('total_marks')
    def _compute_percentage(self):
        self.percentage=(self.total_marks/(self.physics_total_marks+self.maths_total_marks+self.chemistry_total_marks))*100

    @api.depends('maths_marks','chemistry_marks','physics_marks')
    def _compute_total(self):
        self.total_marks=self.maths_marks+self.chemistry_marks+self.physics_marks


import re
from datetime import date,datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread', 'mail.activity.mixin','school.common']
    _sql_constraints = [('roll_number_unique','unique(roll_number)',"The roll number must be unique for each student.")]


    dob=fields.Date(string="Date of Birth", tracking=True, required=True)
    age=fields.Integer(string="Age", compute='_compute_age', tracking=True, required=True)
    gender=fields.Selection(selection=[('male','Male'),('female','Female')], tracking=True, string="Gender", required=True)
    address=fields.Text(string="Address", tracking=True, required=True)
    permanent_address = fields.Text(string="Permanent Address", tracking=True)
    pincode=fields.Char(string="Pincode", tracking=True, required=True)
    contact_no=fields.Char(string="Parent's Contact No.", tracking=True, required=True)
    roll_number=fields.Integer(string="Roll Number")
    blood_group = fields.Selection(selection=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    ], string='Blood Group', tracking=True, required=True)
    percent=fields.Float(string="Percentage", tracking=True, required=True)
    isDiabetic=fields.Boolean(string="Diabetic", tracking=True)
    fee_amount=fields.Monetary(string="Fee Amount",currency_field="currency_id", tracking=True, required=True)
    scholarship_amount = fields.Monetary(string="Scholarship Amount", currency_field="currency_id", tracking=True)
    sports_ids=fields.Many2many(comodel_name='school.sports',relation='school_student_sports_rel',column1='student_id',column2='sport_id', string="Sports",tracking=True)
    currency_id=fields.Many2one(comodel_name='res.currency',string="Currency", default=lambda self:self.env.company.currency_id,tracking=True)
    transportation=fields.Selection(selection=[('Bus','Bus'),('Van','Van')],tracking=True)
    photo=fields.Binary(string="Image", help="Upload Image")
    sign=fields.Binary()
    description = fields.Html(string="Description",tracking=True)
    subjects = fields.Many2many(comodel_name='school.subjects', relation='subject_student_rel', column1='student_id',
                                column2='subject_id', string="Subjects",
                                tracking=True,
                                # domain="[('grade_ids','=',class_id.id)]"
                                )
    final_fee = fields.Monetary(string="Amount to Pay", compute="_compute_amount_to_pay", store=True, currency_field="currency_id",tracking=True)
    my_attachment_ids = fields.One2many(comodel_name='ir.attachment', inverse_name='student_id', string='My Attachments')
    next_birthday = fields.Date(compute="_compute_next_birthday", store=True)
    class_id=fields.Many2one(comodel_name='school.class',string="Class")
    grade = fields.Selection(selection=lambda self: self._get_grade(), string="Grade"   )
    # division = fields.Selection(selection=lambda self: self._get_division_options(), string="Division", required=True)
    user_id=fields.Many2one(comodel_name='res.users',string='Assigned User')
    attendance=fields.Float(string="Attendance")


    @api.model
    def _get_grade(self):
        grades = self.env['school.class'].search([]).mapped('grade')
        return [(grade, grade) for grade in set(grades)]

    # @api.model
    # def _get_division_options(self):
    #     divisions = self.env['school.class'].search([]).mapped('division')
    #     return [(division, division) for division in set(divisions)]

    @api.onchange('grade')
    def _onchange_grade(self):
        if self.grade:
            matching_class = self.env['school.class'].search(domain=[
                ('grade', '=', self.grade),
            ], limit=1)
            if matching_class:
                self.class_id = matching_class.id
            else:
                self.class_id = False

    @api.constrains('contact_no')
    def _check_phone_format(self):
        for record in self:
            contact_no_regex=r'^[6-9]\d{9}$'
            if record.contact_no and not re.match(contact_no_regex, record.contact_no):
                raise ValidationError("Phone number must start with 6-9 and must be of 10 digits.")

    @api.constrains('age')
    def _check_age(self):
        for rec in self:
            if rec.age<=4:
                raise ValidationError("Age should be greater than 4 years.")



    def _compute_next_birthday(self):
        for record in self:
            if record.dob:
                today = date.today()
                dob_date = fields.Date.from_string(record.dob)
                dob_month_day = dob_date.replace(year=today.year)

                if dob_month_day < today:
                    dob_month_day = dob_month_day.replace(year=today.year + 1)

                record.next_birthday = dob_month_day


    @api.depends('fee_amount','scholarship_amount')
    def _compute_amount_to_pay(self):
        for record in self:
            if record.fee_amount:
                record.final_fee=record.fee_amount-record.scholarship_amount


    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                today = datetime.today()
                dob = fields.Datetime.from_string(record.dob)
                age = today.year - dob.year

                # Adjust age if the birthday hasn't occurred yet this year
                if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
                    age -= 1

                record.age = age
                record._check_age()

            else:
                record.age = 0

    def create_report_card(self):
        pass

    def button_click(self):
        return {
            'type':'ir.actions.act_url',
            'url':'http://genevaliberalschool.com'
        }

    def get_permanent_address(self):
        for rec in self:
            if rec.address and not rec.permanent_address:
                rec.write({'permanent_address':rec.address})



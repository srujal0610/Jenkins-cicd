from odoo import fields,models

class CommonFields(models.AbstractModel):
    _name = 'school.common'

    name=fields.Char(string="Name")


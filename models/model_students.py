from odoo import fields, models, api


class StudentErp(models.Model):
    _name = "college.students"
    _description = 'Students Erp'
    _rec_name = 'first_name_id'

    admission_no = fields.Integer('Admission No')
    admission_date = fields.Date('Admission Date')
    first_name_id = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    father = fields.Char('Father')
    mother = fields.Char('Mother')
    communication_address = fields.Char('Communication Address')
    permanent_address = fields.Char('Permanent Address')
    same_as_communication_address = fields.Boolean(
        string='Same As Communication Address', )
    phone = fields.Integer('Phone No')
    email = fields.Char('Email')
    active = fields.Boolean(default=True)



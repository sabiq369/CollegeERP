from odoo import fields, models, api


class Admission(models.Model):
    _name = 'college.admission'
    _description = 'College Admission'
    _rec_name = 'first_name_id'

    first_name_id = fields.Many2one("college.students", string='First Name')
    last_name = fields.Char('Last Time', related='first_name_id.last_name')
    father = fields.Char('Father', related='first_name_id.father')
    mother = fields.Char('Mother', related='first_name_id.mother')
    communication_address = fields.Char('Communication Address',
                                        related='first_name_id'
                                                '.communication_address')
    permanent_address = fields.Char('Permanent Address',
                                    related='first_name_id.permanent_address')
    same_as_communication_address = fields.Boolean(
        'Same As Communication Address',
        related='first_name_id.same_as_communication_address')
    phone = fields.Integer('Phone', related='first_name_id.phone')
    email = fields.Char('Email', related='first_name_id.email')
    course_id = fields.Many2one("college.config.course", string='Course')
    date_of_application = fields.Date('Date Of Application')
    academic_year = fields.Char('Academic Year')
    previous_education_qualification = fields.Selection(
        string='Previous Education Qualification', selection=[
            ('higher_secondary', 'Higher''Secondary'), ('ug', 'UG'),
            ('pg', 'PG')])
    educational_institute = fields.Char('Educational Institute')
    transfer_certificate = fields.Many2many('ir.attachment', 'ir_attach_rel',
                                            'record_relation_id',
                                            'attachment_id',
                                            string="Transfer Certificate",
                                            )
    active = fields.Boolean('active', default=True)
    state = fields.Selection(string='State', default='draft', selection=[
        ('draft', 'Draft'), ('application', 'Application'),
        ('approved', 'Approved'), ('done', 'Done'), ('rejected', 'Rejected')
    ])

    def button_application(self):
        self.write({
            'state': "application"

        })

    def button_approved(self):
        self.write({
            'state': "approved"
        })

    def button_done(self):
        self.write({
            'state': "done"
        })

    def button_rejected(self):
        self.write({
            'state': "rejected"
        })

    def button_draft(self):
        self.write({
            'state': "draft"
        })

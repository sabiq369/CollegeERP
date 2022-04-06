from odoo import fields, models


class Course(models.Model):
    _name = "college.config.course"
    _description = "Configuration Course"

    name = fields.Char('Name')
    category = fields.Selection(string='Category', selection=[
        ('under_graduate', 'Under Graduation'),
        ('post_graduation', 'Post Graduation'), ('diploma', 'Diploma')])
    duration = fields.Integer('Duration')
    no_of_semester = fields.Integer('Number of Semester')
    active = fields.Boolean('Active', default=True)

from odoo import fields, models


class Semester(models.Model):
    _name = 'college.config.semester'
    _description = 'College Semester'

    name = fields.Char('Name', readonly=True)
    no_of_semester = fields.Integer('Number Of Semester')
    course = fields.Many2one('college.config.course', string='Course')
    subject = fields.Char('Subject')
    max_marks = fields.Integer('Maximum Marks')



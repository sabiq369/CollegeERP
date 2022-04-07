from odoo import fields, models


class Semester(models.Model):
    _name = 'college.config.semester'
    _description = 'College Semester'

    name = fields.Char('Name')
    no_of_semester = fields.Integer('Number Of Semester')
    course = fields.Many2one('college.config.course', string='Course')
    syllabus_ids = fields.One2many('college.syllabus', 'subject_id')





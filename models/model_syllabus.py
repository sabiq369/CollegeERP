from odoo import fields, models


class Syllabus(models.Model):
    _name = 'college.syllabus'
    _description = 'College Syllabus'

    subject = fields.Char('Subject')
    max_marks = fields.Integer('Maximum Marks')
    subject_id = fields.Many2one('college.config.semester')

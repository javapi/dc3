# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Penalty(models.Model):
    _name = 'dc3.penalty'

    name = fields.Char('Name',index=True)
    worker_id = fields.Many2one('dc3.worker', 'Woker')
    plant_id = fields.Many2one('dc3.plant', 'Plant')
    date = fields.Date('Penalty date')
    hied_company = fields.Many2one('dc3.hired_company', 'Company')
    section = fields.Many2one('dc3.section', 'Section')
    penalty = fields.Selection([],'Penalty')
    comment = fields.Text('Comments')

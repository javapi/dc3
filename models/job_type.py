# -*- coding: utf-8 -*-

from odoo import fields, models, api

class JobType(models.Model):
    _name = 'dc3.job_type'

    name = fields.Char('Name',index=True)
    description = fields.Text('Description')
    plant_id = fields.Many2one('dc3.plant', 'Plant')

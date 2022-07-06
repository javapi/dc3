# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Certification(models.Model):
    _name = 'dc3.certification'

    name = fields.Char('Name',index=True)
    description = fields.Text('Description')
    plant_id = fields.Many2one('dc3.plant', 'Plant')

# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Area(models.Model):
    _name = 'dc3.area'

    name = fields.Char('Name')
    description = fields.Text('Description')
    plant_id = fields.Many2one('dc3.plant', 'Plant')
    

# -*- coding: utf-8 -*-

from odoo import fields, models, api

class speciality(models.Model):
    _name = 'dc3.speciality'

    name = fields.Char('Name',index=True)
    description = fields.Text('Description')
    plant_id = fields.Many2one('dc3.plant', 'Plant')

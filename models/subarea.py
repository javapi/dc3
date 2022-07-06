# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Subarea(models.Model):
    _name = 'dc3.subarea'

    name = fields.Char('Name')
    description = fields.Text('Description')
    area = fields.Many2one('dc3.area', 'Area   ')

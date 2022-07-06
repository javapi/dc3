# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Responsable(models.Model):
    _name = 'dc3.responsable'

    name = fields.Char('Name',index=True)
    plant_id = fields.Many2one('dc3.plant', 'Plant')

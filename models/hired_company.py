# -*- coding: utf-8 -*-

from odoo import fields, models, api

class HiredCompany(models.Model):
    _name = 'dc3.hired_company'

    name = fields.Char('Name',index=True)
    description = fields.Text('Description')
    plant_id = fields.Many2one('dc3.plant', 'Plant')
    quantity = fields.Integer('Quantity')
    services = fields.Integer('Services')

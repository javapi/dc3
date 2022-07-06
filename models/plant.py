# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Plant(models.Model):
    _name = 'dc3.plant'

    name = fields.Char('Name',index=True)
    description = fields.Text('Description')

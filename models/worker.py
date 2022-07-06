# -*- coding: utf-8 -*-

from odoo import fields, models, api

class Worker(models.Model):
    _name = 'dc3.worker'

    name = fields.Char('Name',index=True)
    plant_id = fields.Many2one('dc3.plant', 'Plant')
    nss = fields.Char('NSS')
    partner_number = fields.Integer('Partner number')
    code = fields.Integer('Code')
    temporality = fields.Selection('')
    admision = fields.Date('Admision')
    supervisor = fields.Text('Supervirsor')
    state = fields.Selection('')
    discharge = fields.Date('Discharge')
    discharge_reason = fields.Text('Dischage reason')
    hired_company_id = fields.Many2one('dc3.hired_company', 'Company')
    speciality_id = fields.Many2one('dc3.speciality', 'speciality')
    job_position_id = fields.Many2one('dc3.job_position','Job position')
    responsable_id = fields.Many2one('dc3.responsabe','Responsable')
    worker_type_id = fields.Many2one('d3.worker_type','Woker type')
    job_type_id = fields.Many2one('dc3.job_type', 'job_type')

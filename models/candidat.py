# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Candidat(models.Model):
    _name = 'candidat.candidat'
    _description = 'Candidat description'
    
    name = fields.Char()
    num_ins = fields.Integer()

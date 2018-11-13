# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Formateur(models.Model):
    _name = 'formateur.formateur'
    _description = 'Formateur description'
    
    name = fields.Char()
    matricule = fields.Integer()
    diplome = fields.Char()
    

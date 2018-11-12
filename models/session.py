# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Session(models.Model):
    _name = 'session.session'
    _description = 'session description'

    name = fields.Char()
    nb_participants = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    duree = fields.Char()
    state = fields.Selection([])

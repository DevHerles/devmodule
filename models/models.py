# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class DevModule(models.Model):
    _name = 'devmodule.devmodule'

    LIST_VARIABLE = []

    name = fields.Char()
    value = fields.Integer(help="Solamente n[umeros enteros.")
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    birthdate = fields.Date(string=u'Fecha de nacimiento')
    yearsold = fields.Integer(string="Edad", compute="_years_old", store=True)
    status = fields.Selection(selection=[('si', 'SI'), ('no', 'NO')])
    valid = fields.Selection(
        string='Muestra v[alida', 
        selection=[
            ('si', 'SI'),
            ('no', 'NO')
            ],
        compute='_valid', store=True,
        default='no'
        )

    mylist = fields.Selection(LIST_VARIABLE, 'Field Label')

    def _selection(self):
        return [('bar','BAR'), ('foo', 'FOO')]

    selection = fields.Selection(_selection, 'Selection demo')

    def __init__(self, pool, cr):
        """Add a new state value"""
        LIST_VARIABLE = [('value1', 'String 1'), ('value2', 'String 2')]
        return LIST_VARIABLE

    @api.depends('status')
    def _valid(self):
        if (self.status):
            self.valid = self.status
        else:
            self.valid = 'no'

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    @api.depends('birthdate')
    def _years_old(self):
        edad = 0
        if self.birthdate:
            edad = (datetime.now().date() - datetime.strptime(self.birthdate, '%Y-%m-%d').date()).days / 365
        self.yearsold = edad

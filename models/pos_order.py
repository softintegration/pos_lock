# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = 'pos.order'

    locked = fields.Boolean(default=True)

    def action_lock(self):
        self._action_lock()

    def action_unlock(self):
        self._action_unlock()

    def _action_lock(self):
        self.write({'locked': True})

    def _action_unlock(self):
        self.write({'locked': False})



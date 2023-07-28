# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import fields, models


class Website(models.Model):
    _inherit = 'website'

    whatsapp_number = fields.Char(string="Whatsapp Number")
    whatsapp_check_out = fields.Boolean(string="Whatsapp Checkout")


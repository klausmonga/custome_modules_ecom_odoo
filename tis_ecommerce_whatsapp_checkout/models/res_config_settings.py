# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd.
# - © Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    whatsapp_number = fields.Char(string='WhatsApp Number', related='website_id.whatsapp_number',
                                  config_parameter='tis_ecommerce_whatsapp_checkout.whatsapp_number')
    whatsapp_checkout = fields.Selection([
        ('public_users', 'Public Users'),
        ('login_users', 'Login Users'),
    ], default='public_users', string="WhatsApp Checkout",
        config_parameter='tis_ecommerce_whatsapp_checkout.whatsapp_checkout')

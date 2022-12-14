# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields, models


class SaleOrderMassMail(models.TransientModel):
    _name="so.quote.mail"
    
    sale_order_ids = fields.Many2many('sale.order',string="Sale Orders",required=True, domain=[('state', 'in', ['draft', 'sent', 'sale'])])
   

    def send_mail(self):
        vals = self.sale_order_ids
        for order in vals:
            template_id = self.env.ref('sale.email_template_edi_sale')
            if template_id:
                template_id.send_mail(order.id, force_send=True)
        return True
        
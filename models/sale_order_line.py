# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    order_date_order = fields.Datetime(string='Order Date',related='order_id.date_order',readonly=True)
from odoo import api, fields, models

class SalesOrder(models.Model):
    _inherit = "sale.order"
    sale_description = fields.Char(string="Sale Description")

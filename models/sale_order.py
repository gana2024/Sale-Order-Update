from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_products_qty = fields.Float(string="Total Quantity", compute='_compute_total_products_qty', store=True)

    @api.depends('order_line.product_uom_qty')
    def _compute_total_products_qty(self):
        for order in self:
            order.total_products_qty = sum(order.order_line.mapped('product_uom_qty'))

    product_names = fields.Text(string="Product Names", compute='_compute_product_names')

    @api.depends('order_line.product_id')
    def _compute_product_names(self):
        for order in self:
            order.product_names = ', '.join(order.order_line.mapped('product_id.name'))

    def print_report(self):
        return self.env.ref('sales.order_summary_report').report_action(self)





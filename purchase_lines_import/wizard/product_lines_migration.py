
# -*- coding: utf-8 -*-
##############################################################################
#
#
##############################################################################

from odoo import _, api, fields, models
from datetime import date, datetime


class OrderLinesMigration(models.Model):
    """
    Account move line reconcile wizard.
    """
    _name = 'order.lines.migration'

    order_date = fields.Date('Order date', required=True)
    supplier_id = fields.Many2one('res.partner', string="Supplier", required=True)
    order_type = fields.Selection([('requisition','Requisition'),('done_order','Done Order')],string="Order type")

    def create_migration_order(self):
   
        order_data = self.env['purchase.order.line.data']
        order_created = self.env['purchase.order']
        line  = [] 
        tax = []
        if 'active_ids' in self._context and self._context['active_ids']:
            data = order_data.search(
                [('id', 'in', self._context.get('active_ids', []))])
            for rec in data:

                all_tax = 0.0
                vals = rec._prepare_compute_all_values()
                taxes = rec.taxes_id.compute_all(
                    vals['price_unit'],
                    vals['currency_id'],
                    vals['product_qty'],
                    vals['product'],
                    vals['partner'])

                if rec.taxes_id:
                    for tx in rec.taxes_id:
                        all_tax += tx.amount
                line += [(0,6 ,{
                    'product_id': rec.product_id.id,
                    'product_qty' : rec.product_qty,
                    'price_unit' :rec.price_unit,
                    'discount' : rec.discount ,
                    'name' :rec.name,
                    'date_planned' : rec.date_planned,
                    'product_uom' : rec.product_uom.id,
                    'price_subtotal':taxes['total_included'] - (taxes['total_excluded'] * (rec.discount / 100)),
                    'price_total':taxes['total_included'] - (taxes['total_excluded'] * (rec.discount / 100)),

                    'taxes_id':rec.taxes_id.ids,
                    'migration_id': rec.id

                  
                })]  
            order_id = order_created.create({
                'date_order': self.order_date,
                'partner_id' : self.supplier_id.id,
                'order_line' : line
                })
            
            for rec_line in order_id.order_line:
                rec_line.taxes_id = rec_line.migration_id.taxes_id.ids
               
        
        if self.order_type == 'done_order':
            order_id.state = 'purchase'

        view_mode = 'tree,form'
        return {
            'name': str(self.order_date) + ''+self.supplier_id.name,
            'view_type': 'form',
            'view_mode':  'form',
            'res_model': 'purchase.order',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': order_id.id,
        }
            


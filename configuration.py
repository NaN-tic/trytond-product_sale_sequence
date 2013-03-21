# This file is part product_sale_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = [
    'ProductConfiguration',
    'ProductConfigurationCompany',
]
__metaclass__ = PoolMeta


class ProductConfiguration:
    'Product Configuration'
    __name__ = 'product.configuration'
    salable_sequence = fields.Function(fields.Many2One('ir.sequence', 'Salable Sequence',
        domain=[
            ('code', '=', 'product.product'),
        ], required=True),'get_fields', setter='set_fields')


class ProductConfigurationCompany:
    'Product Configuration Company'
    __name__ = 'product.configuration.company'
    salable_sequence = fields.Many2One('ir.sequence', 'Salable sequence', 
        domain=[
            ('code', '=', 'product.product'),
        ], required=True)

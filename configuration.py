# This file is part product_sale_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = [
    'ProductConfiguration',
    'ProductConfigurationCompany',
]
__metaclass__ = PoolMeta


class ProductConfiguration:
    __name__ = 'product.configuration'
    salable_sequence = fields.Function(fields.Many2One('ir.sequence', 'Salable Sequence',
        domain=[
            ('code', '=', 'product.product'),
        ]),'get_fields', setter='set_fields')


class ProductConfigurationCompany:
    __name__ = 'product.configuration.company'
    salable_sequence = fields.Many2One('ir.sequence', 'Salable sequence', 
        domain=[
            ('code', '=', 'product.product'),
        ])

#This file is part product_sale_sequence module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Product']
__metaclass__ = PoolMeta


class Product:
    'Product Product'
    __name__ = 'product.product'

    @classmethod
    def get_sale_sequence(cls):
        Sequence = Pool().get('ir.sequence')
        Configuration = Pool().get('product.configuration')

        config = Configuration(1)
        code = Sequence.get_id(config.salable_sequence.id)
        return code

    @classmethod
    def create(cls, vlist):
        Template = Pool().get('product.template')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            tpl = Template.read([values.get('template')], ['salable'])[0]
            if not values.get('code') and tpl.get('salable'):
                values['code'] = cls.get_sale_sequence()
        return super(Product, cls).create(vlist)

    @classmethod
    def write(cls, products, vals):
        super(Product, cls).write(products, vals)
        for product in products:
            if product.template.salable and not product.code:
                if not vals.get('code'):
                    cls.write([product], {
                        'code': cls.get_sale_sequence()
                        })

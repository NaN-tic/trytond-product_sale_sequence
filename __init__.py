#This file is part product_sale_sequence module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *
from .configuration import *

def register():
    Pool.register(
        Configuration,
        Product,
        module='product_sale_sequence', type_='model')

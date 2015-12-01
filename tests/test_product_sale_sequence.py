# This file is part of the product_sale_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductSaleSequenceTestCase(ModuleTestCase):
    'Test Product Sale Sequence module'
    module = 'product_sale_sequence'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductSaleSequenceTestCase))
    return suite
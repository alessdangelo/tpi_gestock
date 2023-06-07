from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from .models import t_borrow, t_article, t_categories, t_cupboard, t_products, t_room, t_types
from django.contrib.auth.models import User


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = t_products.objects.create(proName='Test Product', proNote='Test Description', proBoughtDate="2023-06-03", proBoughtPrice=20.0,
                                                 fkCategory=t_categories.objects.create(catName="Test Category"), fkType=t_types.objects.create(typName="Test Type"))

    def test_product_name(self):
        self.assertEqual(self.product.proName, 'Test Product')

    def test_product_description(self):
        self.assertEqual(self.product.proNote, 'Test Description')

    def test_product_date(self):
        self.assertEqual(self.product.proBoughtDate, '2023-06-03')

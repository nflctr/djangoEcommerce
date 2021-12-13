from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        data = self.data1
        # Test Category model data insertion/types/field attributes
        self.assertTrue(isinstance(data, Category))
        # Test Category model default name
        self.assertEqual(str(data), 'django')

    def test_category_url(self):
        data = self.data1
        response = self.client.post(reverse('store:category_list', args=[data.slug]))
        # Test Category model slug and URL reverse
        self.assertEqual(response.status_code, 200)


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price='19.99', image='default1')
        self.data2 = Product.objects.create(category_id=1, title='django advanced', created_by_id=1, slug='django-advanced', price='22.99', image='default2')

    def test_products_model_entry(self):
        data = self.data1
        # Test Products model data insertion/types/field attributes
        self.assertTrue(isinstance(data, Product))
        # Test Products model default name
        self.assertEqual(str(data), 'django beginners')

    def test_products_url(self):
        # Test Products model slug and URL reverse
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        response = self.client.post(reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(url, '/django-beginners')
        self.assertEqual(response.status_code, 200)

    # def test_products_custom_manager_basic(self):
    #     data = Product.products.all()
    #     self.assertEqual(data.count(), 1)                           # Test Products model custom manager returns only active products

from urllib.parse import urlencode

from django.test import TestCase

from src.products.models import Product

class ProductModelTests(TestCase):

    def test_product_creation(self):

        """
        ensure_price_is_positive should results True for products where price is zero or positive
        """
        prod = Product(name="test",price=1.99, stockpile=10, can_be_sold=True)
        prod.save()
        self.assertEqual((prod.price == 1.99), True)
        self.assertEqual((prod.stockpile == 10), True)
        self.assertEqual((prod.name == "test"), True)
        self.assertTrue(prod.can_be_sold)


class ProductsViewsTests(TestCase):

    fixtures = ["users.json", "products.json"]

    def setUp(self):
        self.response = self.client.login(username="joe", password="bar")

    def test_index_view_with_no_products(self):
        """
        If no products exist, an appropriate message should be displayed.
        """
        Product.objects.all().delete()
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no products present.")
        self.assertQuerysetEqual(response.context["products"], [])

    def test_index_view_with_products(self):
        """
        If products exist, they should be displayed.
        """
        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "new product")
        self.assertEqual(len(response.context["products"]), 3)

    def test_delete_view(self):
        """
        Should delete the product
        """
        response = self.client.delete("/products/delete_product/1")

        self.assertEqual(response.status_code, 200)

        all_products_query = Product.objects.all()
        self.assertEqual(len(all_products_query), 2)

    def test_create_view(self):
        """
        Should create the product
        """
        response = self.client.post("/products/create_product", {"name": "created product", "price": 4.44, "stockpile": 33, "can_be_sold": True})

        self.assertEqual(response.status_code, 201)

        all_products_query = Product.objects.all()
        self.assertEqual(len(all_products_query), 4)

    def test_update_view(self):
        """
        Should update the product
        """
        response = self.client.patch("/products/update_product/1", urlencode({"name": "updated product", "price": 4.44, "stockpile": 33, "can_be_sold": False}), content_type="text")

        self.assertEqual(response.status_code, 200)

        all_products_query = Product.objects.all()
        self.assertEqual(len(all_products_query), 3)
        product_query = Product.objects.get(id=1)
        self.assertEqual(product_query.name, "updated product")
        self.assertEqual(product_query.price, 4.44)
        self.assertEqual(product_query.stockpile, 33)
        self.assertEqual(product_query.can_be_sold, False)

import json

from django.test import TestCase

from products.models import Product

class ProductModelTests(TestCase):

    def test_product_creation(self):

        """
        ensure_price_is_positive should results True for products where price is zero or positive
        """
        prod = Product(name="test",price=1.99, stockpile=10)
        prod.save()
        self.assertEqual((prod.price == 1.99), True)
        self.assertEqual((prod.stockpile == 10), True)
        self.assertEqual((prod.name == "test"), True)


class ProductsViewsTests(TestCase):

    def test_index_view_with_no_products(self):
        """
        If no products exist, an appropriate message should be displayed.
        """
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no products present.")
        self.assertQuerysetEqual(response.context["products"], [])

    def test_index_view_with_products(self):
        """
        If no products exist, an appropriate message should be displayed.
        """
        prod = Product(name="new product",price=1.99, stockpile=10)
        prod.save()

        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "new product")
        self.assertEqual(len(response.context["products"]), 1)

    def test_delete_view(self):
        """
        Should delete the product
        """
        prod = Product(name="new product",price=1.99, stockpile=10)
        prod.save()
        prod2 = Product(name="new product 2",price=5.99, stockpile=17)
        prod2.save()

        response = self.client.delete("/products/delete_product/1")

        self.assertEqual(response.status_code, 200)

        all_products_query = Product.objects.all()
        self.assertEqual(len(all_products_query), 1)

    def test_create_view(self):
        """
        Should create the product
        """
        prod = Product(name="new product",price=1.99, stockpile=10)
        prod.save()

        response = self.client.post("/products/create_product", {"name": "created product", "price": 4.44, "stockpile": 33})

        self.assertEqual(response.status_code, 201)

        all_products_query = Product.objects.all()
        self.assertEqual(len(all_products_query), 2)

    def test_update_view(self):
        """
        Should update the product
        """
        prod = Product(name="product",price=1.99, stockpile=10)
        prod.save()

        response = self.client.post("/products/update_product/1", {"name": "updated product", "price": 4.44, "stockpile": 33})

        self.assertEqual(response.status_code, 201)

        all_products_query = Product.objects.all()
        self.assertEqual(len(all_products_query), 1)
        product_query = Product.objects.get(id=1)
        self.assertEqual(product_query.name, "updated product")
        self.assertEqual(product_query.price, 4.44)
        self.assertEqual(product_query.stockpile, 33)

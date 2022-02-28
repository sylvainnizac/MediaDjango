from urllib.parse import urlencode

from django.test import TestCase

from src.products.models import Product
from src.sells.models import Sell

class SellModelTests(TestCase):

    def test_sell_creation(self):

        """
        Create Sell in db
        """
        prod = Product(name="Bananas",price=1.99, stockpile=10)
        prod.save()
        sell = Sell(
            client_name="C. Sanzos",
            product=prod,
            unit_price=prod.price,
            quantity=2
            )
        sell.save()
        self.assertEqual((sell.client_name == "C. Sanzos"), True)
        self.assertEqual((sell.quantity == 2), True)
        self.assertEqual((sell.product == prod), True)
        self.assertEqual((sell.unit_price == 1.99), True)


class SellsViewsTests(TestCase):

    fixtures = ["users.json", "products.json", "sells.json"]

    def setUp(self):
        self.response = self.client.login(username="joe", password="bar")

    def test_index_view_with_no_sells(self):
        """
        If no sells exist, an appropriate message should be displayed.
        """
        Sell.objects.all().delete()
        response = self.client.get("/sells/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no sells present.")
        self.assertQuerysetEqual(response.context["sells"], [])

    def test_index_view_with_sells(self):
        """
        If sells exist, they should be displayed.
        """
        response = self.client.get("/sells/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "apple")
        self.assertContains(response, "orange")
        self.assertContains(response, "Dupont")
        self.assertContains(response, "Dupond")
        self.assertEqual(len(response.context["sells"]), 2)

    def test_delete_view(self):
        """
        Should delete the sell
        """
        response = self.client.delete("/sells/delete_sell/1")

        self.assertEqual(response.status_code, 200)

        all_sells_query = Sell.objects.all()
        self.assertEqual(len(all_sells_query), 1)

    def test_create_view(self):
        """
        Should create the sell
        """
        response = self.client.post("/sells/create_sell", {"client_name": "Nestor", "quantity": 3, "product": 1})

        self.assertEqual(response.status_code, 201)

        all_sells_query = Sell.objects.all()
        self.assertEqual(len(all_sells_query), 3)

    def test_update_view(self):
        """
        Should update the sell
        """
        response = self.client.patch("/sells/update_sell/1", urlencode({"client_name": "Nestor", "quantity": 4, "product": 2}), content_type="text")

        self.assertEqual(response.status_code, 201)

        all_sells_query = Sell.objects.all()
        self.assertEqual(len(all_sells_query), 2)
        sell_query = Sell.objects.get(id=1)
        self.assertEqual(sell_query.client_name, "Nestor")
        self.assertEqual(sell_query.unit_price, 2.00)
        self.assertEqual(sell_query.quantity, 4)
        self.assertEqual(sell_query.product.id, 2)

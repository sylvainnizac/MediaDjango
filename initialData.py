import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediaDjango.settings')

import django
django.setup()

from products.models import Product
from sells.models import Sell


def populate():
    p1 = add_product(name="apple", price=1.0, stockpile=17)

    p2 = add_product(name="orange", price=2.0, stockpile=8)

    s1 = add_sell(client_name="Dupond", product=p2, quantity=10, unit_price=2.0)

    s2 = add_sell(client_name="Dupont", product=p1, quantity=15, unit_price=1.0)

    # Print out what we have added to the database.
    for p in Product.objects.all():
        print("- {}".format(str(p)))

    for s in Sell.objects.all():
        print("- {}".format(str(s)))


def add_product(name, price=0, stockpile=0):
    p = Product(name=name, stockpile=stockpile, price=price)
    p.save()
    return p


def add_sell(client_name, product, quantity, unit_price):
    s = Sell(client_name=client_name, product=product, quantity=quantity, unit_price=unit_price)
    s.save()
    return s


# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()

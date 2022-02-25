import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MediaDjango.settings')

import django
django.setup()

from products.models import Product


def populate():
    add_product(name="apple",
        price=1.0,
        stockpile=17)

    add_product(name="orange",
        price=5.5,
        stockpile=8)

    # Print out what we have added to the user.
    for p in Product.objects.all():
        print("- {}".format(str(p)))

def add_product(name, price=0, stockpile=0):
    p = Product.objects.get_or_create(name=name)[0]
    p.stockpile=stockpile
    p.price=price
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()
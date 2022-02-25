from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods

from sells.models import Sell
from products.models import Product

def index(request):
    all_sells = Sell.objects.all()
    all_products = Product.objects.all()

    context_dict = {
        "sells": all_sells,
        "products": all_products,
        "empty_message": _("There are no sells present.")
    }

    return render(request, 'sells/index.html', context_dict)

@require_http_methods(["POST"])
def create_sell(request):
    print(request.POST)
    return HttpResponse(status=201)
    # form_data = ProductForm(request.POST)
    # 
    # if form_data.is_valid():
    #     form_data.save()
    #     return HttpResponse(status=201)
    # else:
    #     return HttpResponse(form_data.errors.as_json(), status=400)

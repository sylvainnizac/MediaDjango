from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from products.forms import ProductForm
from products.models import Product


@login_required
@require_http_methods(["GET"])
def index(request):
    """
        main page to display and manage products
    """
    all_products = Product.objects.all()

    context_dict = {"products": all_products,
                    "empty_message": _("There are no products present.")}

    return render(request, 'products/index.html', context_dict)


@login_required
@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    """
        delete product from id
        returns
            200 if OK
            404 if product doesn't exist
    """
    product = get_object_or_404(Product, id=product_id)

    if product:
        Product.objects.filter(id=product_id).delete()

    return HttpResponse(status=201)


@login_required
@require_http_methods(["POST"])
def create_product(request):
    """
        create new product from form
        returns
            200 if OK
            400 if error in creation
    """
    form_data = ProductForm(request.POST)

    if form_data.is_valid():
        form_data.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(form_data.errors.as_json(), status=400)


@login_required
@require_http_methods(["POST"])
def update_product(request, product_id):
    """
        update product from form
        returns
            200 if OK
            400 if error in update
    """
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(form_data.errors.as_json(), status=400)
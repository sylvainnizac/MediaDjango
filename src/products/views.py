from django.core import serializers
from django.http import HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from src.products.forms import ProductForm
from src.products.models import Product


@login_required
@require_http_methods(["GET"])
def index(request):
    """
        main page to display and manage products
    """
    all_products = Product.objects.all()
    form = ProductForm()

    context_dict = {"products": all_products,
                    "form": form,
                    "empty_message": "There are no products present."}

    return render(request, 'products/index.html', context_dict)


@login_required
@require_http_methods(["DELETE"])
def delete_product(request, product_id):
    """
        delete product from id
        returns
            200 if OK
            404 if product to delete doesn't exist
    """
    product = get_object_or_404(Product, id=product_id)

    if product:
        Product.objects.filter(id=product_id).delete()

    return HttpResponse(status=200)


@login_required
@require_http_methods(["POST"])
def create_product(request):
    """
        create new product from form
        returns
            201 if OK
            400 if error in creation
    """
    form_data = ProductForm(request.POST)

    if form_data.is_valid():
        form_data.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(form_data.errors.as_json(), status=400)


@login_required
@require_http_methods(["PATCH"])
def update_product(request, product_id):
    """
        update product from form
        returns
            200 if OK
            404 if product to update doesn't exist
            400 if error in update
    """
    # get original object
    product = get_object_or_404(Product, id=product_id)
    # transform patch data
    query_dict = QueryDict(request.body)
    # update original object
    form = ProductForm(query_dict or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(form_data.errors.as_json(), status=400)
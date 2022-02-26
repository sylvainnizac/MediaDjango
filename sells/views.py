from django.http import HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from sells.forms import SellForm
from sells.models import Sell


@login_required
@require_http_methods(["GET"])
def index(request):
    """
        main page to display and manage sells
    """
    all_sells = Sell.objects.all()
    form = SellForm()

    context_dict = {
        "sells": all_sells,
        "form": form,
        "empty_message": _("There are no sells present.")
    }

    return render(request, 'sells/index.html', context_dict)


@login_required
@require_http_methods(["POST"])
def create_sell(request):
    """
        create new sell from form
        returns
            200 if OK
            400 if error in creation
    """
    form = SellForm(request.POST)
    if form.is_valid():
        new_sell = form.save()
        # unit_price is extracted from product to keep sell total price constant even if product price changes
        new_sell.unit_price = new_sell.product.price
        new_sell.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(form.errors.as_json(), status=400)


@login_required
@require_http_methods(["PATCH"])
def update_sell(request, sell_id):
    """
        update sell from form
        returns
            200 if OK
            400 if error in update
    """
    # get original object
    sell = get_object_or_404(Sell, id=sell_id)
    # transform patch data
    query_dict = QueryDict(request.body)
    # update original object
    form = SellForm(query_dict or None, instance=sell)

    if form.is_valid():
        updated_sell = form.save()
        # unit_price is extracted from product to keep sell total price constant even if product price changes
        updated_sell.unit_price = updated_sell.product.price
        updated_sell.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(form.errors.as_json(), status=400)


@login_required
@require_http_methods(["DELETE"])
def delete_sell(request, sell_id):
    """
        delete sell from id
        returns
            200 if OK
            404 if sell doesn't exist
    """
    sell = get_object_or_404(Sell, id=sell_id)

    if sell:
        Sell.objects.filter(id=sell_id).delete()

    return HttpResponse("Deleted")

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    context_dict = {"boldmessage": _("Products says hey there world!")}

    return render(request, 'products/index.html', context_dict)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

@require_http_methods(["GET"])
def index(request):
    """
        main page to display login form
    """

    context_dict = {
        # "sells": all_sells,
        # "form": form,
        # "empty_message": _("There are no sells present.")
    }

    return render(request, 'users/index.html', context_dict)


@require_http_methods(["POST"])
def login_view(request):
    """
        check credentials and log user
    """

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            login(request, user)
            return HttpResponse('/sells/')
        else:
            return HttpResponse("Your account is disabled.")
    else:
        print("Invalid login details: {0}, {1}".format(username, password))
        return HttpResponse("Invalid login details supplied.")


@require_http_methods(["GET"])
def logout_view(request):
    """
        logout user
    """
    logout(request)
    return HttpResponse('/')

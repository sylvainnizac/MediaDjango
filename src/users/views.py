from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

@require_http_methods(["GET"])
def index(request):
    """
        main page to display login form
    """

    context_dict = {}

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
            return HttpResponse('/sells/', status=200)
        else:
            return HttpResponse("Your account is disabled.", status=403)
    else:
        return HttpResponse("Invalid login details supplied.", status=401)


@require_http_methods(["GET"])
def logout_view(request):
    """
        logout user
    """
    logout(request)
    return HttpResponse('/')

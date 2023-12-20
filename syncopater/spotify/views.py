from django.shortcuts import render, redirect
from .api.auth_code import get_auth_code
from .api.auth_token import auth_token

# Create your views here.

def auth_code(request):
    if request.session.get('access_token') is not None:
        return redirect('test')
    elif request.session.get('access_token') is None:
        get_auth_code()
        return HttpResponse(status=204)
    else:
        return render(request, 'test.html', {'json': 'auth code failed... sad face :('})

#spotify callback
def callback(request):
    json = auth_token(request.GET.get('code'))
    # store the access token in the session
    request.session['access_token'] = json['access_token']
    return redirect('test')

def test(request):
    return render(request, 'test.html')
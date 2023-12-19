from django.shortcuts import render
from .api.auth_code import get_auth_code
from .api.auth_token import auth_token

# Create your views here.

def auth_code(request):
    get_auth_code()
    return render(request, 'test.html', {'json': 'auth code'})

#spotify callback
def callback(request):
    json = auth_token(request.GET.get('code'))
    return render(request, 'test.html', {'json': json})
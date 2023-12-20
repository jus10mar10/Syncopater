from django.shortcuts import render, redirect, HttpResponse
from .api.auth_code import get_auth_code
from .api.auth_token import auth_token
from .api.utils import is_access_token_valid
from .api.functions import get_total_songs_in_library

# Create your views here.

def auth_code(request):
    access_token = request.session.get('access_token')
    if access_token is not None and is_access_token_valid(access_token):
        return render(request, 'test.html', {'json': 'Already authenticated!'})
    else:
        get_auth_code()
        return render(request, 'index.html')

def callback(request):
    code = request.GET.get('code')
    if code:
        json = auth_token(code)
        if 'access_token' in json:
            request.session['access_token'] = json['access_token']
            return redirect('test')
    
    return render(request, 'test.html', {'json': 'Authentication failed... sad face :('})

def test(request):
    access_token = request.session.get('access_token')
    if access_token is not None and is_access_token_valid(access_token):
        total_artists = get_total_songs_in_library(access_token)
        return render(request, 'test.html', {'artist_count': f'You have {total_artists} artists in your library!'})
    else:
        return render(request, 'test.html', {'json': 'You are not authenticated!'})
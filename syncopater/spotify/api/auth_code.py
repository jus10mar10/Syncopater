import webbrowser
from urllib.parse import urlencode 
from .utils import get_secrets
from django.conf import settings

def get_auth_code():
    client_id, client_secret = get_secrets()

    auth_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": f"{settings.BASE_URL}/spotify/callback/",
        "scope": "user-library-read"
    }

    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers), new=0)

    return
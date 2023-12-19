import webbrowser
from urllib.parse import urlencode 
from .utils import get_secrets

def get_auth_code():
    client_id, client_secret = get_secrets()

    auth_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": "http://localhost:8080/spotify/callback",
        "scope": "user-library-read"
    }

    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    return
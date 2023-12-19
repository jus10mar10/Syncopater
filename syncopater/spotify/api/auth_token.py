import base64
import requests
from .utils import get_secrets

def auth_token(code):

    client_id, client_secret = get_secrets()

    # Spotify requres the client id and secret to be encoded in base64 in format client_id:client_secret
    encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

    # Basic is required in the header

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:8080/spotify/callback"
    }

    r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

    return r.json()
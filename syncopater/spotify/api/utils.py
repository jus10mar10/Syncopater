from dotenv import load_dotenv
import os    
import requests

def get_secrets():
    # Load .env file
    load_dotenv()

    # Gets the authorization code from Spotify
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    return client_id, client_secret

def is_access_token_valid(access_token):
    # Make a request to a protected Spotify API endpoint to check token validity
    spotify_api_url = 'https://api.spotify.com/v1/me'  # Replace with the appropriate Spotify endpoint
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(spotify_api_url, headers=headers)

    if response.status_code == 200:
        # Token is valid
        return True
    elif response.status_code == 401:
        # Token is invalid or has expired
        return False
    else:
        # Handle other response codes as needed
        return False
    
def sign_out(request):
    request.session.clear()
    return redirect('auth_code')

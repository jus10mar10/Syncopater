from dotenv import load_dotenv
import os    

def get_secrets():
    # Load .env file
    load_dotenv()

    # Gets the authorization code from Spotify
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    return client_id, client_secret
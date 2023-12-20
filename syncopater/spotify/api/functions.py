import requests

def get_total_songs_in_library(access_token):
    # Spotify API endpoint for getting user's saved tracks
    spotify_api_url = 'https://api.spotify.com/v1/me/tracks'

    # Set headers
    headers = {'Authorization': f'Bearer {access_token}'}

    offset = 0

    total = 0

    response = requests.get(spotify_api_url, headers=headers, params={'offset': offset})

    total += response.json()['total']

    return total


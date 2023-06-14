import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from urllib.parse import urlparse, parse_qs

def get_credentials():
    if os.path.isfile('credentials.json'):
        with open('credentials.json', 'r') as f:
            credentials = json.load(f)
    else:
        credentials = {}
        credentials['Client ID'] = input('Please enter your Client ID: ')
        credentials['Client Secret'] = input('Please enter your Client Secret: ')
        credentials['Redirect URI'] = input('Enter a Redirect URI. This can be any valid URL (e.g., http://localhost/): ')

        with open('credentials.json', 'w') as f:
            json.dump(credentials, f)
    
    return credentials

def get_playlist_id(url):
    # Parse the URL
    parsed = urlparse(url)
    # Get the ID
    playlist_id = parsed.path.split('/')[-1]
    return playlist_id

def save_playlist(playlist, file_path):
    with open(file_path, 'w') as file:
        for item in playlist['tracks']['items']:
            track = item['track']
            file.write(f"{track['name']} - {track['artists'][0]['name']}\n")

def main():
    credentials = get_credentials()
    
    # Spotify API setup
    scope = "playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=credentials['Client ID'], 
        client_secret=credentials['Client Secret'], 
        redirect_uri=credentials['Redirect URI'], 
        scope=scope))
    
    # Get playlist
    playlist_url = input('Enter the Spotify playlist link: ')
    playlist_id = get_playlist_id(playlist_url)
    playlist = sp.playlist(playlist_id)

    # Save playlist to file
    playlist_name = playlist['name']
    output_dir = os.path.join(os.getcwd(), 'playlists')
    os.makedirs(output_dir, exist_ok=True)
    save_playlist(playlist, os.path.join(output_dir, f'{playlist_name}.txt'))

if __name__ == "__main__":
    main()

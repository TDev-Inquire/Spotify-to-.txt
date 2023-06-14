import spotipy
from spotipy.oauth2 import SpotifyOAuth
import getpass

print("This program requires Spotify Developer credentials to access the Spotify Web API.")
print("To get these credentials:")
print("1. Visit the Spotify Developer Dashboard (https://developer.spotify.com/dashboard/)")
print("2. Click on 'CREATE AN APP'")
print("3. Fill out the necessary information and click 'CREATE'")
print("4. Your Client ID and Client Secret will be shown on the next page")

# Obtain the Spotify developer credentials from the user
client_id = getpass.getpass('Please enter your Client ID: ')
client_secret = getpass.getpass('Please enter your Client Secret: ')

# Get the redirect URI from the user
print("Enter a Redirect URI. This can be any valid URL (e.g., http://localhost/)")
redirect_uri = input('Redirect URI: ')

# Set up Spotify OAuth
scope = 'playlist-read-private'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get the playlist URL from the user
playlist_url = input('Enter the Spotify playlist link: ')

# Extract the playlist id from the URL
playlist_id = playlist_url.split('/')[-1]

# Fetch the playlist data
playlist = sp.playlist(playlist_id)

# Open a file to write the songs to
with open(f'{playlist["name"]}.txt', 'w') as f:
    # Go through each track in the playlist
    for item in playlist['tracks']['items']:
        track = item['track']
        # Write the track to the file in the format "song title - artist"
        f.write(f'{track["name"]} - {track["artists"][0]["name"]}\n')

print(f'Successfully exported playlist "{playlist["name"]}"')

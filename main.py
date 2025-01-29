import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

scope = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
	client_secret=SPOTIPY_CLIENT_SECRET,
	redirect_uri=SPOTIPY_REDIRECT_URI,
	scope=scope))

def show_current_song():
	"""working"""
	track = sp.currently_playing()
	if track and track['is_playing']:
		song = track['item']['name']
		artist = track['item']['artists'][0]['name']
		print(f"({song} - {artist}")
	else:
		print("nothing to show")

if __name__ == "__main__":
	while True:
		show_current_song()
		time.sleep(5)

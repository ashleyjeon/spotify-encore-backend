import os
from dotenv import load_dotenv
import spotipy 

load_dotenv()

def get_spotify_client(): 
    auth_manager = spotipy.oauth2.SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("REDIRECT_URI"), 
        scope="user-top-read playlist-modify-public playlist-modify-private"
    )
    return spotipy.Spotify(auth_manager=auth_manager)
from fastapi import APIRouter, Request 
from fastapi.responses import RedirectResponse 
import os 
from dotenv import load_dotenv 
from spotipy.oauth2 import SpotifyOAuth 

load_dotenv() 

router = APIRouter() 

spotify_oauth = SpotifyOAuth( 
    client_id=os.getenv("SPOTIFY_CLIENT_ID"), 
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"), 
    redirect_uri=os.getenv("REDIRECT_URI"), 
    scope="user-top-read playlist-modify-public playlist-modify-private"
)

@router.get("/login")
def login(): 
    url = spotify_oauth.get_authorize_url() 
    return RedirectResponse(url)

@router.get("/callback")
def callback(request: Request): 
    code = request.query_params.get("code")
    if not code:
        return {"error": "No code provided in callback"}
    
    token_info = spotify_oauth.get_access_token(code)
    return { "access_token": token_info["access_token"], "refresh_token": token_info["refresh_token"] }
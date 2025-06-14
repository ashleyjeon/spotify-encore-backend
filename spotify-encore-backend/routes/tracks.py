from fastapi import APIRouter 
from utils.spotify_client import get_spotify_client 

router = APIRouter() 

@router.get("/top-tracks")
def get_top_tracks(): 
    sp_client = get_spotify_client() 
    top_tracks = sp_client.current_user_top_tracks(limit=5) 
    print(top_tracks)
    # return {"top_tracks": [t["name"] for t in top_tracks["items"]]}
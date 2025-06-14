from fastapi import FastAPI 
from auth import router as auth_router 
from routes.tracks import router as tracks_router 
# from routes.playlists import router as artists_router

app = FastAPI() 

app.include_router(auth_router, prefix="/auth") 
app.include_router(tracks_router, prefix="/top-tracks") 
# app.include_router(artists_router, prefix="/artists")

@app.get("/")
def root(): 
    return {"message": "Spotify Encore Backend is live"}
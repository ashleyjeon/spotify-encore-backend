from fastapi import FastAPI 
from starlette.middleware.sessions import SessionMiddleware
from auth import router as auth_router 
# from routes.tracks import router as tracks_router 
# from routes.playlists import router as artists_router

import os 
from dotenv import load_dotenv 
load_dotenv()

app = FastAPI() 

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET_KEY"))

app.include_router(auth_router, prefix="/auth") 
# app.include_router(tracks_router, prefix="/top-tracks") 
# app.include_router(artists_router, prefix="/artists")

@app.get("/")
def root(): 
    return {"message": "Spotify Encore Backend is live"}
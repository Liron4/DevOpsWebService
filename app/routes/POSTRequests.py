from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import redis.asyncio as redis

router = APIRouter()

r = redis.Redis(host='redis', port=6379, decode_responses=True) # variables names should be meaningful, r is not a good name, could be redis_client or similar

class Song(BaseModel):
    title: str
    youtube_link: str

@router.post("/{username}")
async def create_user(username: str):
    user_key = f"user:{username}"

    if await r.exists(user_key):
        raise HTTPException(status_code=409, detail="User already exists")

    await r.hset(user_key, "initialized", "true")
    return {"message": "User created successfully"} # break line before return for better readability

@router.post("/{username}/songs")
async def add_song(username: str, song: Song):
    user_key = f"user:{username}"
    if not await r.exists(user_key): # break line before if for better readability
        raise HTTPException(status_code=404, detail="User not found")
    
    song.youtube_link = song.youtube_link.lower() # For consistency

    song_title_key = f"song:{username}:{song.title}"
    song_link_key = f"songlink:{username}:{song.youtube_link}"

    if await r.exists(song_title_key):
        raise HTTPException(status_code=409, detail="Song's title already exists under this user")

    if await r.exists(song_link_key):
        raise HTTPException(status_code=409, detail="Song's link already exists under this user")

    await r.set(song_title_key, song.youtube_link) 
    await r.set(song_link_key, song.title)

    return {"message": "Song added successfully"}
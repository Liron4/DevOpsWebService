from fastapi import APIRouter, HTTPException
import redis.asyncio as redis

router = APIRouter()

r = redis.Redis(host='redis', port=6379, decode_responses=True) # variables names should be meaningful, r is not a good name, could be redis_client or similar

@router.get("/users")
async def get_all_users():
    keys = await r.keys("user:*")
    if not keys: # break line before if for better readability
        raise HTTPException(status_code=404, detail="No users found")

    users = [key.split(":")[1] for key in keys]
    return {"users": users} # break line before return for better readability

@router.get("/{username}/songs")
async def get_user_songs(username: str):
    user_key = f"user:{username}"
    if not await r.exists(user_key): # break line before if for better readability
        raise HTTPException(status_code=404, detail="User not found")

    song_keys = await r.keys(f"song:{username}:*")
    songs = []

    for song_key in song_keys:
        song_title = song_key.split(":")[2]
        youtube_link = await r.get(song_key)
        songs.append({"title": song_title, "youtube_link": youtube_link})

    return {"username": username, "songs": songs}
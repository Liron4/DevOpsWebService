from fastapi import APIRouter, HTTPException
import redis.asyncio as redis

router = APIRouter()
r = redis.Redis(host='redis', port=6379, decode_responses=True) # variables names should be meaningful, r is not a good name, could be redis_client or similar

@router.delete("/{username}")
async def delete_user(username: str):
    user_key = f"user:{username}"

    if not await r.exists(user_key):
        raise HTTPException(status_code=404, detail="User not found")

    # Find all song keys related to this user
    keys = await r.keys(f"song:{username}:*")
    keys += await r.keys(f"songlink:{username}:*")
    keys.append(user_key)

    await r.delete(*keys)
    return {"message": f"User '{username}' and all their songs have been deleted successfully."} # break line before return for better readability


@router.delete("/{username}/songs/{song_title}")
async def delete_song(username: str, song_title: str):
    user_key = f"user:{username}"

    if not await r.exists(user_key):
        raise HTTPException(status_code=404, detail="User not found")

    song_title_key = f"song:{username}:{song_title}"
    
    if not await r.exists(song_title_key):
        raise HTTPException(status_code=404, detail="Song not found for this user")

    # Get the youtube link to remove the reverse key too - code shouldnt include comments, they should be self-explanatory
    youtube_link = await r.get(song_title_key)
    song_link_key = f"songlink:{username}:{youtube_link}"

    await r.delete(song_title_key, song_link_key)

    return {"message": f"Song '{song_title}' deleted successfully for user '{username}'."}

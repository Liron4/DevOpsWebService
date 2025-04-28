from fastapi import FastAPI
import uvicorn
from app.routes.POSTRequests import router as post_router

app = FastAPI(title="Playlist Server API")

# POST routes
app.include_router(post_router, prefix="/POST")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
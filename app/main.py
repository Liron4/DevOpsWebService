from fastapi import FastAPI
import uvicorn
from app.routes.POSTRequests import router as post_router
from app.routes.DELETERequests import router as delete_router

app = FastAPI(title="Playlist Server API")

# POST routes
app.include_router(post_router, prefix="/POST")

# DELETE routes
app.include_router(delete_router, prefix="/DELETE")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
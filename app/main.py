from fastapi import FastAPI
from app.miniature import Miniature
from typing import List, Optional

app = FastAPI()


@app.post("/api/miniatures")
async def create_miniatures(miniature: Miniature) -> str:
    return "success"


# bulk add miniature api


@app.get("/api/miniatures")
async def get_miniatures() -> List[Miniature]:
    return []


@app.get("/api/miniatures/{id}")
async def get_miniatures(id: int) -> Optional[Miniature]:
    return None


@app.put("/api/miniatures/{id}")
async def edit_miniatures(id: int) -> str:
    return "success"


@app.delete("/api/miniatures/{id}")
async def delete_miniatures(id: int) -> str:
    return "success"


# login api

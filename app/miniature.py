from pydantic import BaseModel
from typing import List


class Miniature(BaseModel):
    id: int
    name: str
    description: str = ""
    image_url: str = ""
    tags: List[str] = []
    created_at: str = None
    r_time: str = None

from pydantic import BaseModel
from typing import List


class Miniature(BaseModel):
    id: int
    name: str
    description: str = ""
    image_url: str = ""
    num_battles: int = 0
    tags: List[str] = []

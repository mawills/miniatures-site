from pydantic import BaseModel
from typing import List


class Miniature(BaseModel):
    id: int
    name: str
    description: str = ""
    image_url: str = ""
    # created_at: str

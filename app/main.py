from fastapi import FastAPI, HTTPException, status
from app.miniature import Miniature
from app.DatabaseConnection import DatabaseConnection
from typing import List, Optional

app = FastAPI()

db = DatabaseConnection()
conn = db.connect()
cursor = conn.cursor()


@app.get("/")
def root() -> str:
    return "Hello world! I'm alive!"


@app.post("/api/miniatures", status_code=status.HTTP_201_CREATED)
async def create_miniatures(miniature: Miniature) -> str:
    cursor.execute(
        """INSERT INTO miniatures (id, name, description, image_url, tags) VALUES (%s, %s, %s, %s, %s) RETURNING *""",
        (
            miniature.id,
            miniature.name,
            miniature.description,
            miniature.image_url,
            miniature.tags,
        ),
    )
    new_miniature = cursor.fetchall()
    conn.commit()

    return new_miniature


# bulk add miniature api


@app.get("/api/miniatures")
async def get_miniatures() -> List[Miniature]:
    cursor.execute("""SELECT * FROM miniatures""")
    miniatures = cursor.fetchall()

    return miniatures


@app.get("/api/miniatures/{id}")
async def get_miniatures(id: int) -> Optional[Miniature]:
    cursor.execute("""SELECT * FROM miniatures WHERE id=%s""", (id,))
    miniature = cursor.fetchone()

    if not miniature:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not found.",
        )

    return miniature


@app.put("/api/miniatures/{id}")
async def edit_miniatures(id: int, miniature: Miniature) -> Optional[Miniature]:
    cursor.execute(
        """UPDATE miniatures SET name=%s, description=%s, image_url=%s, tags=%s WHERE id=%s RETURNING *""",
        (
            miniature.name,
            miniature.description,
            miniature.image_url,
            miniature.tags,
            id,
        ),
    )
    updated_miniature = cursor.fetchone()

    if not updated_miniature:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not found.",
        )

    conn.commit()

    return updated_miniature


@app.delete("/api/miniatures/{id}")
async def delete_miniatures(id: int) -> str:
    # Can update this function or use a new one to update rtime rather than truly delete from db
    cursor.execute("""DELETE FROM miniatures WHERE id=%s RETURNING *""", (id,))
    deleted_miniature = cursor.fetchone()

    if not deleted_miniature:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not found.",
        )

    conn.commit()

    return deleted_miniature

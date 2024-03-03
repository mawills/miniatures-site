from fastapi import FastAPI, HTTPException, status, Depends, Response
from . import models
from .database import engine, get_db
from .schemas import Miniature
from sqlalchemy.orm import Session
from typing import List, Optional

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> str:
    return "Hello world! I'm alive!"


@app.post("/api/miniatures", status_code=status.HTTP_201_CREATED)
async def create_miniatures(miniature: Miniature, db: Session = Depends(get_db)):
    new_miniature = models.Miniature(**miniature.dict())
    db.add(new_miniature)
    db.commit()
    db.refresh(new_miniature)

    return {"data": new_miniature}


@app.get("/api/miniatures")
async def get_miniatures(db: Session = Depends(get_db)):
    miniatures = db.query(models.Miniature).all()
    return {"data": miniatures}


@app.get("/api/miniatures/{id}")
async def get_miniatures(id: int, db: Session = Depends(get_db)):
    miniature = db.query(models.Miniature).filter(models.Miniature.id == id).first()

    if not miniature:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not found.",
        )

    return {"data": miniature}


@app.put("/api/miniatures/{id}")
async def edit_miniatures(
    id: int, updated_miniature: Miniature, db: Session = Depends(get_db)
):
    query = db.query(models.Miniature).filter(models.Miniature.id == id)
    miniature = query.first()

    if miniature == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"miniature with id {id} not found.",
        )

    query.update(updated_miniature.dict(), synchronize_session=False)

    db.commit()

    return {"data": updated_miniature}


@app.delete("/api/miniatures/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_miniatures(id: int, db: Session = Depends(get_db)) -> Response:
    # Can update this function or use a new one to update rtime rather than truly delete from db
    miniature = db.query(models.Miniature).filter(models.Miniature.id == id)

    if miniature.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"miniature with id {id} not found.",
        )

    miniature.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

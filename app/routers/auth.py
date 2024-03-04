from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router = APIRouter(tags=["Authentication"])


@router.post("/api/login")
async def login(
    user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.email)
        .first()
    )

    if not user or not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials"
        )

    return "success"

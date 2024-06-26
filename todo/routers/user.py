from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from .. import schemas,database
from .. repositary import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/',response_model= schemas.User)
def create_user(request:schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model= schemas.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.get_user(id,db)
from fastapi import FastAPI, Depends
from . import models, schemas, crud
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from typing import List

# ? DB作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ? Sessionの獲得
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ? indexページ [get]
# @app.get("/")
# async def index():
#     return {"message": "success"}

# ? Read処理
# ? ユーザー取得 [get]
@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return {"users": users}


# ? 部屋取得 [get]
@app.get("/room", response_model=List[schemas.Room])
async def read_rooms(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return {"rooms": rooms}


# ? 会議室取得 [get]
@app.get("/bookings", response_model=List[schemas.Booking])
async def read_bookings(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return {"bookings": bookings}




# ? ユーザー登録画面 [post]
@app.post("/users",response_model=schemas.User)
async def create_user(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    return crud.create_user(db,schemas.User)



# ? 部屋登録画面 [post]
@app.post("/room", response_model=schemas.Room)
async def create_room(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    return crud.create_room(db,schemas.Room)


# ? 会議室登録画面 [post]
@app.post("/bookings")
async def create_boooking(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    return crud.create_booking(db,schemas.Booking)


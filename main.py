from fastapi import FastAPI
import datetime
from pydantic import BaseModel, Field

# ? 予約モデル
class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

# ? ユーザーモデル
class User(BaseModel):
    user_id: int
    username: str = Field(max_length=12)

# ? 会議室モデル
class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int


app = FastAPI()


# ? indexページ [get]
@app.get("/")
async def index():
    return {"message": "success"}


# ? ユーザー登録画面 [post]
@app.post("/users")
async def user(user: User):
    return {"user":user}


# ? 予約画面 [post]
@app.post("/room")
async def room(room: Room):
    return {"room": room}

import datetime
from pydantic import BaseModel, Field

# * FastAPIサイド 型の定義

class CreateBooking(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime


# ? 予約用
class Booking(CreateBooking):
    booking_id: int

    class Config:
        orm_mode = True

# ? ユーザー作成用
class UserCreate(BaseModel):
    username: str = Field(max_length=12)


# ? ユーザーモデル
class User(UserCreate):
    user_id: int
    username: str = Field(max_length=12)

    class Config:
        orm_mode = True


# ? 会議室作成用
class CreateRoom(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int

# ? 会議室モデル
class Room(CreateRoom):
    room_id: int

    class Config:
        orm_mode = True

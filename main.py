from fastapi import FastAPI
from .sql_app.schemas import User,Room,Booking

app = FastAPI()


# ? indexページ [get]
@app.get("/")
async def index():
    return {"message": "success"}


# ? ユーザー登録画面 [post]
@app.post("/users")
async def user(user: User):
    return {"user": user}


# ? 部屋登録画面 [post]
@app.post("/room")
async def room(room: Room):
    return {"room": room}


# ? 会議室登録画面 [post]
@app.post("/bookings")
async def user(booking: Booking):
    return {"booking": booking}

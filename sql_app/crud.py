from sqlalchemy.orm import Session
from . import models, schemas

# * ------------- READ -------------
# ? ユーザー情報取得用
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit=limit).all()

# ? 会議室情報取得用
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit=limit).all()
    
# ? 予約情報取得用    
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit=limit).all()

# * ------------- CREATE -------------
# ? ユーザー登録
def create_user(db :Session, user: schemas.User):
    db_user = models.User(username = user.username) # ? インスタンスの生成
    db.add(db_user)
    db.commit() # ? DBに反映
    db.refresh(db_user) # ? DBをリフレッシュ
    return db_user
    

# ? 会議室登録
def create_room(db :Session, room: schemas.Room):
    db_room = models.Room(room_name = room.room_name, capacity = room.capacity) # ? インスタンスの生成
    db.add(db_room)
    db.commit() # ? DBに反映
    db.refresh(db_room) # ? DBをリフレッシュ
    return db_room
    

# ? 会議室登録
def create_booking(db :Session, booking: schemas.Booking):
    db_booking = models.Booking(
        user_id = booking.user_id,
        room_id = booking.room_id,
        booking_id = booking.booking_id,
        booked_num = booking.booked_num,
        start_datetime = booking.start_datetime,
        end_datetime = booking.end_datetime
        ) # ? インスタンスの生成

    db.add(db_booking)
    db.commit() # ? DBに反映
    db.refresh(db_booking) # ? DBをリフレッシュ
    return db_booking
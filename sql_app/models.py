from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

# * DB定義 テーブル作成
# ? ユーザーテーブル
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


# ? 会議室テーブル
class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)


# ? 予約テーブル
class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.user_id, ondelete='SET NULL'), nullable=False)
    room_id = Column(Integer, ForeignKey(Room.room_id, ondelete='SET NULL'), nullable=False)
    book_num = Column(Integer)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)

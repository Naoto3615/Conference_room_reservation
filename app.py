import streamlit as st
import json
import requests
import random
import datetime

# * フロントエンド streamlit作成
# ? サイドバー作成
page = st.sidebar.selectbox('Chose your page', ['users', 'rooms', 'bookings'])

# ? usersを選択した場合の処理
if page == 'users':
    st.title('ユーザー登録画面')

    with st.form(key='user'):
        # ? フォームの中身
        # user_id: int = random.randint(0, 10)
        username: str = st.text_input('ユーザー名', max_chars=12)

        data = {
            'username': username
        }

        submitted = st.form_submit_button(label="リクエスト送信")

        # ? 送信ボタンを押した際の挙動
        if submitted:

            url = 'http://127.0.0.1:8000/users'
            # ? 送る内容
            res = requests.post(url,
                                data=json.dumps(data))
            # st.write(res.status_code)
            if res.status_code == 200:
                st.success('ユーザー登録完了')
                


# ? roomを選択した場合の処理
elif page == 'rooms':
    st.title('会議室登録画面')

    with st.form(key='rooms'):
        # ? フォームの中身
        # room_id: int = random.randint(0, 10)
        room_name: str = st.text_input('会議室名', max_chars=12)
        capacity: int = st.number_input('定員', step=1, max_value=300)

        data = {
            # 'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }

        submitted = st.form_submit_button(label="リクエスト送信")

        # ? 送信ボタンを押した際の挙動
        if submitted:

            url = 'http://127.0.0.1:8000/room'
            # ? 送る内容
            res = requests.post(url,
                                data=json.dumps(data))
            if res.status_code == 200:
                st.write("会議室登録成功")


# ? bookingを選択した場合の処理
elif page == 'bookings':
    st.title('会議室予約画面')

    with st.form(key='bookings'):
        # ? フォームの中身
        booking_id: int = random.randint(0, 10)
        # ! 後でuser,roomモデルと紐付けすること
        user_id: int = random.randint(0, 10)
        room_id: int = random.randint(0, 10)

        booked_num: int = st.number_input('予約人数', step=1)
        date = st.date_input('日付を入力', min_value=datetime.date.today())
        start_time = st.time_input('開始時刻: ', value=datetime.time(hour=9, minute=0))
        end_time = st.time_input('終了時刻: ', value=datetime.time(hour=20, minute=0))

        data = {
            'booking_id': booking_id,
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(    
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ).isoformat(),
            'end_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
            ).isoformat()
        }

        submitted = st.form_submit_button(label="リクエスト送信")

        # ? 送信ボタンを押した際の挙動
        if submitted:
            st.json(data)

            url = 'http://127.0.0.1:8000/bookings'
            # ? 送る内容
            res = requests.post(url,
                                data=json.dumps(data))
            st.write('送っている情報')
            st.write(res.json())

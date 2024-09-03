import streamlit as st
import json
import requests
import random

page = st.sidebar.selectbox('Chose your page', ['users', 'rooms'])

if page == 'users':
    st.title('APIテスト画面（ユーザー）')

    with st.form(key='user'):
        # ? フォームの中身
        user_id: int = random.randint(0, 10)
        username: str = st.text_input('ユーザー名', max_chars=12)

        data = {
            'user_id': user_id,
            'username': username
        }

        submitted = st.form_submit_button(label="リクエスト送信")

        # ? 送信ボタンを押した際の挙動
        if submitted:
            st.json(data)

            url = 'http://127.0.0.1:8000/users'
            # ? 送る内容
            res = requests.post(url,
                                data=json.dumps(data))
            st.write(res.json())
            st.write(data)

elif page == 'rooms':
    st.title('APIテスト画面（会議室）')

    with st.form(key='rooms'):
        # ? フォームの中身
        room_id: int = random.randint(0, 10)
        room_name: str = st.text_input('会議室名', max_chars=12)
        capacity: int = st.number_input('定員', step=1, max_value=300)

        data = {
            'room_id': room_id,
            'room_name': room_name,
            'capacity': capacity
        }

        submitted = st.form_submit_button(label="リクエスト送信")

        # ? 送信ボタンを押した際の挙動
        if submitted:
            st.json(data)

            url = 'http://127.0.0.1:8000/room'
            # ? 送る内容
            res = requests.post(url,
                                data=json.dumps(data))
            st.write(res.json())
            st.write(data)

import streamlit as st
import json
import requests
import random

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

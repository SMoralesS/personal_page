import json
import streamlit as st


class HomePage:
    def __init__(self, data_url: str = './streamlit_app/utils/data.json') -> None:
        with open(data_url, 'r') as data_file:
            self.data = json.load(data_file)

    def add_logo(self):
        st.markdown(
            f"""
            <style>
                [data-testid="stSidebarNav"] {{
                    background-image: url({self.data.get('logo_url', '')});
                    background-repeat: no-repeat;
                    padding-top: 120px;
                    background-position: 70px 30px;
                    background-size: 200px 200px;
                }}
                [data-testid="stSidebarNav"]::before {{
                    content: "";
                    margin-left: 20px;
                    margin-top: 20px;
                    font-size: 30px;
                    position: relative;
                    top: 100px;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )

    def add_signature(self):
        st.title(self.data.get('name', ''))
        st.subheader(self.data.get('profession', ''))

    def add_intro(self):
        st.write(self.data.get('personal_description', ''))
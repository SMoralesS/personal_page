import json
import streamlit as st
import utils.utils


class HomePage:
    def __init__(
        self, 
        personal_info_data_path: str = './streamlit_app/utils/personal_data.json',
        ) -> None:
        with open(personal_info_data_path, 'r') as data_file:
            self.personal_data = json.load(data_file)
        

    def add_logo(self):
        st.markdown(
            f"""
            <style>
                [data-testid="stSidebarNav"] {{
                    background-image: url({self.personal_data.get('logo_url', '')});
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
        st.title(self.personal_data.get('name', ''))
        st.subheader(self.personal_data.get('profession', ''))

    def add_intro(self):
        st.write(self.personal_data.get('personal_description', ''))
    
    def add_socials(self):
        linkedin_url = self.personal_data.get('linkedin', '')
        linkedin_title = 'Linkedin' if linkedin_url else ''
        linkedin_logo = 'https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg' if linkedin_url else ''
        
        github_url = self.personal_data.get('github', '')
        github_title = 'Github' if linkedin_url else ''
        github_logo = 'https://cdn-icons-png.flaticon.com/512/3291/3291695.png' if github_url else ''
        
        with st.sidebar:
            cols = st.columns(4)
            with cols[1]:
                st.markdown(
                    utils.utils.img_url_to_html(linkedin_logo, linkedin_url, linkedin_title, '80%', '80%'),
                    unsafe_allow_html=True
                )
                 
            with cols[2]:
                st.markdown(
                    utils.utils.img_url_to_html(github_logo, github_url, github_title, '70%', '70%'),
                    unsafe_allow_html=True
                )

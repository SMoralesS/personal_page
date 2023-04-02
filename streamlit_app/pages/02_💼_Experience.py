import streamlit as st

# set_page_config must be the first streamlit command in the file
st.set_page_config(
    page_title="Experience",
    page_icon="💼",
)

from utils.itemize_page import *


def main():
    experience_page = ItemizePage(data_path="streamlit_app/user_data/experience_data.jsonl")
    experience_page.add_logo()
    st.title("Professional Experience")   
    experience_page.write_itemize_html()
    experience_page.add_socials()

if __name__ == "__main__":
    main()
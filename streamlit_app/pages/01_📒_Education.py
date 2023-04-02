import streamlit as st

# set_page_config must be the first streamlit command in the file
st.set_page_config(
    page_title="Education",
    page_icon="📒",
)

from utils.itemize_page import *


def main():
    education_page = ItemizePage(data_path="streamlit_app/user_data/formal_education_data.jsonl")
    education_page.add_logo()
    st.title("Education")   
    education_page.write_itemize_html()

if __name__ == "__main__":
    main()
from utils.itemize_page import *

st.set_page_config(
    page_title="Education",
    page_icon="👋",
)

def main():
    education_page = ItemizePage(data_path="streamlit_app/utils/formal_education_data.jsonl")
    education_page.add_logo()
    st.title("Education")
    education_page.write_itemize_html()

if __name__ == "__main__":
    main()
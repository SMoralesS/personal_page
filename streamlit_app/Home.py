from utils.home_page import *

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

def main():
    home_page = HomePage()
    home_page.add_logo()
    home_page.add_signature()
    home_page.add_intro()

if __name__ == "__main__":
    main()

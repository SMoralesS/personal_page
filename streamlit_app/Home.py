from streamlit_app.utils.home_page import *

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

def main():
    import os
    st.write(os.listdir())
    home_page = HomePage()
    home_page.add_logo()
    home_page.add_signature()
    home_page.add_intro()
    text =  "<ul>\
            <li>Coffee</li>\
            <li>Tea</li>\
            <li>Milk</li>\
        </ul>" 

    st.components.v1.components.html(text, width=200, height=200)

if __name__ == "__main__":
    main()

from utils import *

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)


def main():
    add_logo()
    st.title("Santiago Morales")
    st.subheader("Data Scientist - Physicist - Applied Mathemathician")
    st.markdown(
        """
      This is a personal web page to exemplify some of my work as data scientist while allow me to train my abilities using streamlit and other tools.
    """
    )


if __name__ == "__main__":
    main()

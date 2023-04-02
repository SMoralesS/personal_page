import plotly.graph_objects as go

from streamlit_app.utils.home_page import *

st.set_page_config(
    page_title="Example page",
    page_icon="📊",
)


def main():

    st.title("Ona example page.")

    with st.sidebar:
        st.subheader(
            "This is the sidebar"
            )
        model_name = st.selectbox(
            'Select model:',
            ['model_q', 'model_y']
        proportion_threshold = st.slider('Proportion Threshold:', 0., 2.5, 0.9)


if __name__ == "__main__":
    main()

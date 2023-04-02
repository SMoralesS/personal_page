import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def img_url_to_html(img_url: str, href: str='', title: str='', height: str=None, width: str=None):
    '''
    Input: 
    img_url: location of the image. 
    href: Hyperlink you want to link to.
    title: Title of the image.
    height: height of the image as string including the dimensionality (px, %, ...).
    width: width of the image as string including the dimensionality (px, %, ...).
    '''
    href = href if href else '#'
    html = f"""
        <a href=\"{href}\">
        <img src=\"{img_url}\" alt=\"{title}\" width=\"{width}\" height=\"{height}\">
        </a>
    """
    return html
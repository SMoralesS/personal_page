import streamlit as st
from typing import Union

class ItemizePage:
    def __init__(self, title: Union[str, None] = None):
        self.title = title

text =  "<ul>\
            <li>Coffee</li>\
            <li>Tea</li>\
            <li>Milk</li>\
        </ul>" 

st.components.v1.components.html(text, width=200, height=200)

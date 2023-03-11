import streamlit as st

text =  "<ul>\
            <li>Coffee</li>\
            <li>Tea</li>\
            <li>Milk</li>\
        </ul>" 

st.components.v1.components.html(text, width=200, height=200)

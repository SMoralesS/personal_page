import json

import streamlit as st
from typing import Union
from utils.utils import local_css
from Home import HomePage

class ItemizePage(HomePage):
    def __init__(self, data_path: str, title: Union[str, None] = None):
        super().__init__()
        self.title = title
        self.data_path = data_path
        self.load_data()

    def load_data(self):
        self.itemize_data = []
        with open(self.data_path) as f:
            for line in f:
                self.itemize_data.append(json.loads(line))

    def write_itemize_html(self):
        local_css("streamlit_app/utils/css_itemize.css")
        text =  "<ul>"
        for item in self.itemize_data:
            text += "<li>"
            text += f"<span class=\"title\">{item.get('title')}</span>"
            text += f"<div class=\"info\">"
            text += f"<span class=\"date\">{item.get('from_date')} - {item.get('to_date')}</span><br>"
            text += f"<span class=\"company\"><a href=\"{item.get('institution_url', '#')}\">{item.get('institution', '')}</a></span>.<br>"
            if "thesis" in item.keys():
                text += f"<span>Thesis: {item.get('thesis')}<br></span>"
            text += f"<span class=\"location\">{item.get('location')}</span>"
            text += "</div>"
            text += "</li><br>"
        text += "</ul>"

        st.components.v1.html(text, height=16000)

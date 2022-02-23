import json
from io import StringIO

import streamlit as st

from unseal.interface import utils

def on_file_upload():
    if st.session_state.uploaded_file is None:
        return
    
    data = json.loads(StringIO(st.session_state.uploaded_file.getvalue().decode('utf-8')).read())
    
    st.session_state.visualization = data
    print(data)
    
    for layer in range(len(data)):
        html_str = st.session_state.visualization[f'layer_{layer}']
        with st.expander(f'Layer {layer}'):
            st.components.v1.html(html_str, height=600)


# create sidebar
with st.sidebar:
    st.file_uploader(
        label='Upload Visualization', 
        accept_multiple_files=False,
        on_change=on_file_upload,
        help='Upload the visualizations as an json of html files.', 
        key='uploaded_file'
    )
import streamlit as st
import numpy as np
import pandas as pd
import os
import git

from utils import get_repo_tags, checkout_repo_tags


st.title('Dataset Versioning with DVC')

version_dataset = get_repo_tags(os.getcwd())

choice = st.selectbox('Dataset Version', version_dataset)

st.write(choice)

if choice is not None:
    # checkout repository tags
    checkout_repo_tags(os.getcwd(), choice)

st.header('Upload Dataset')

cats_col, dogs_col = st.columns(2)

with cats_col:
    st.subheader('Cats Dataset')

    cat_images = st.file_uploader(
        "Choose a file",
        key='cats_uploader',
        type=['png', 'jpg'],
        accept_multiple_files=True)

    for file in cat_images:
        st.write("filename:", file.name)

        with open(os.path.join('data/cats', file.name), 'wb') as f:
            f.write((file).getbuffer())

        st.success('File Saved')

    cats_list = sorted(os.listdir('data/cats/'))

    st.write(cats_list)

with dogs_col:
    st.subheader('Dogs Dataset')

    dog_images = st.file_uploader(
        "Choose a file",
        key='dogs_uploader',
        type=['png', 'jpg'],
        accept_multiple_files=True)

    for file in dog_images:
        st.write("filename:", file.name)

        with open(os.path.join('data/dogs', file.name), 'wb') as f:
            f.write((file).getbuffer())

        st.success('File Saved')

    dogs_list = sorted(os.listdir('data/dogs/'))

    st.write(dogs_list)

st.header('Save Dataset')
version = st.text_input('Dataset Version', 'v2.0')
st.button('Upload Dataset')
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Namaste",
    page_icon="🙏",
)

image = Image.open('cover.jpg')

st.write("# Welcome to Bank Note Authentication System!")

st.image(image)

st.sidebar.success("Select a page.")

st.markdown(
    """
        An ML classifier web app to classify bank notes whether they are fake or not
    """
    )


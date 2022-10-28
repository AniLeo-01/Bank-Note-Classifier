import requests
import streamlit as st

#define title
st.title("Bank Note Authentication System")
st.write("The model accepts the features of the bank notes and outputs whether it is a bank note or a fake note")

#Input: variance
variance = st.number_input(label="variance")
#Input: skewness
skewness = st.number_input(label="skewness")
#Input: curtosis
curtosis = st.number_input(label="curtosis")
#Input: entropy
entropy = st.number_input(label="entropy")

#on submit
if st.button("Submit"):
    #input to model
    inputs = {
                "variance": variance,
                "skewness": skewness,
                "curtosis": curtosis,
                "entropy": entropy
            }

    #posting inputs to ML API
    response = requests.post("http://127.0.0.1:8000/predict", json=inputs)
    json_response = response.json()
    prediction = json_response.get('Prediction')
    st.subheader(f"The note is a **{prediction}**!")
import json
import requests
import streamlit as st
import pandas as pd

st.title("Prediction History")

option = st.selectbox("Select a Query:", ('View all Prediction History', 
'View Prediction by id', 'Delete Prediction by id', 'Reset all history'))

if option == 'View all Prediction History':
    response = requests.get("http://127.0.0.1:8000/history")
    json_response = response.json()
    if len(json_response[0]) != 0:
        df_response = pd.DataFrame(json_response[0])
        df_response['id'] = df_response['id'].astype(int)
        st.dataframe(df_response.set_index(['id']))
    else:
        st.subheader("History is empty!")

if option == 'View Prediction by id':
    id = st.number_input("Enter the id", min_value=0)
    response = requests.get("http://127.0.0.1:8000/history_by_id", params={"id": id})
    json_response = response.json()
    if json_response is not None:
        id, label, score = st.columns(3)
        id.metric("id", json_response["id"])
        score.metric("Prediction score", json_response['prediction_score'])
        label.metric("Prediction label", json_response['prediction_label'])
    else:
        st.write("id not present in database")

if option == "Delete Prediction by id":
    id = st.number_input("Enter the id", min_value=0)
    button_control = st.button("Delete")
    if button_control:
        response = requests.delete("http://127.0.0.1:8000/history_by_id", params={"id": id}).json()
        if response['Deleted_element'] is not None:
            id, label, score = st.columns(3)
            id.metric("id", response['Deleted_element']["id"])
            score.metric("Prediction score", response['Deleted_element']['prediction_score'])
            label.metric("Prediction label", response['Deleted_element']['prediction_label'])
            st.subheader(f"Successfully Deleted id **{response['Deleted_id']}**")
        else:
            st.subheader(f"id **{response['Deleted_id']}** does not exist!")

if option == "Reset all history":
    button_control = st.button("Clear all history")
    if button_control:
        response = requests.delete('http://127.0.0.1:8000/history')
        response = response.json()
        st.subheader(f"History cleared!\nNumber of deleted records: **{response['Deleted_records']}**")
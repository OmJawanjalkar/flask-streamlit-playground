import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age=st.slider("Select your age:", 0, 100, 25)

st.write(f"You age is {age}")

option = ["python","java","c++","javascript"]
choice = st.selectbox("Select your favorite programming language:", option)
st.write(f"You selected: {choice}")


if name:
   st.write(f"Hello, {name}!")



data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    "Age": [24, 30, 22, 35],
    "City":["New York","Los Angeles","Chicago","Houston"]
    }

st.dataframe(pd.DataFrame(data))

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

if upload_file is not None:
  df=pd.read_csv(upload_file)
  st.write(df)
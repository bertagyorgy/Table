import pandas as pd
import streamlit as st


data = pd.read_csv("generated.csv")
st.write(data)

import streamlit as st
import pandas as pd

# Proyecto Airbnb

df = pd.read_csv("airbnb.csv")
st.write(df)
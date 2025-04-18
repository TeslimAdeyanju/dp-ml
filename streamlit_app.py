import streamlit as st
import pandas as pd
import numpy as np

st.title(' 💎 This is a Diamond Prediction App')

st.info('This app builds on data collection from merchant !')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

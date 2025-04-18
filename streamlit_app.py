import streamlit as st
import pandas as pd
import numpy as np

st.title(' 💎 This is a Diamond Prediction App')

st.info('This app builds on data collection from merchant !')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://github.com/TeslimAdeyanju/4-Portfolio-SDS-CP023-diamond-price-predictor/blob/main/submissions-team/teslim-adeyanju/data.csv')
  df.head()



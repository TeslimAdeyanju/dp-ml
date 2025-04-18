import streamlit as st
import pandas as pd

st.title('💎 Diamond Prediction App')

st.info('This app builds on data collection from merchant!')

with st.expander('Data'):
    st.write('**Raw Data**')
    url = 'https://raw.githubusercontent.com/TeslimAdeyanju/4-Portfolio-SDS-CP023-diamond-price-predictor/main/submissions-team/teslim-adeyanju/data.csv'
    df = pd.read_csv(url)
    st.dataframe(df.head())


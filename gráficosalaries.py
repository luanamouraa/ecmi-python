import streamlit as st
import pandas as pd
st.title('Arquivo csv')
st.caption('Luana Moura')

df = pd.read_csv('salaries.csv', sep=',')
st.dataframe(df) 

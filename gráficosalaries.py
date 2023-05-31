import streamlit as st
import pandas as pd
st.title('Arquivo csv')
st.caption('Luana Moura')

df = pd.read_csv('ds_salaries', sep=',')
st.dataframe(df) 


import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

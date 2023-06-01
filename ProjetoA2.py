import streamlit as st
import pandas as pd
from transformers import pipeline

st.title('Projeto A2')
st.caption('Aluna: Luana Rodrigues de Melo Moura')

model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
sentiment_task = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

def sentimento(texto):
    sentimento = sentiment_task(texto)
    return sentimento[0]['label']

with st.form('texto_teste'):
    texto = st.text_area('Insira o texto para testar o modelo:')
    envia_texto = st.form_submit_button(label='Analisar')

with st.form('arquivo_pandas'):
    arquivo = st.file_uploader('Insira o arquivo para classificar o sentimento:', type='csv')
    variavel = st.text_input('Insira o nome da variável com o texto:', value='texto')
    envia_arquivo = st.form_submit_button(label='Analisar')

if envia_texto:
    st.header('Resultado:')
    st.text(f'O sentimento do texto é: {sentimento(texto)}')

if envia_arquivo:
    st.header('Resultado:')
    df = pd.read_csv(arquivo)
    df['sentimento'] = df[variavel].apply(sentimento)
    st.subheader('Amostra do dataframe classificado')
    st.dataframe(df.head(10))
    st.bar_chart(df['sentimento'].value_counts())
    st.download_button(label='Baixar arquivo classificado', data=df.to_csv(), file_name='classificado.csv', mime='text/csv')

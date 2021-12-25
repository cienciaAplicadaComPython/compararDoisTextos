import streamlit as st
import pandas as pd

st.title('Tenho vocabulário para isso?')

'Esta aplicação ajuda você a cruzar palavras de duas fontes de entrada e retornar as palavras em comum e diferentes.'

'Casos de uso:'
'\ti) Comparar os vocabulários ensinado e de uma música para aulas de inglês;'
'\tii) Encontrar palavras desconhecidas em um texto;'
'\tiii) Antecipar o vocabulário necessário para um filme.'

st.subheader('Use o app!')

entradaDeTextoPrimaria = st.file_uploader('Anexe o primeiro arquivo .txt com as palavras separadas por espaço:', type= ['txt'])
entradaDeTextoSecundaria = st.file_uploader('Anexe o segundo arquivo .txt com as palavras separadas por espaço:', type= ['txt'])

botaoFoiSelecionado = st.button('Faça a mágica')

if botaoFoiSelecionado:
  if not(entradaDeTextoPrimaria and entradaDeTextoSecundaria):
    'Anexe os dois arquivos!'
  else:
    dataframePrimaria = pd.read_csv(entradaDeTextoPrimaria, header = None)
    st.write(dataframePrimaria)
    dataframeSecundaria = pd.read_csv(entradaDeTextoSecundaria, header = None)
    st.write(dataframeSecundaria)
  

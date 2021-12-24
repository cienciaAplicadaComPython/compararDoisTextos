import streamlit as st

st.title('Tenho vocabulário para isso?')

'Esta aplicação ajuda você a cruzar palavras de duas fontes de entrada e retornar as palavras em comum e diferentes.'

'Casos de uso:'
'\ti) Comparar os vocabulários ensinado e de uma música para aulas de inglês;'
'\tii) Encontrar palavras desconhecidas em um texto;'
'\tiii) Antecipar o vocabulário necessário para um filme.'

st.subheader('Use o app!')

entradaDeTextoPrimaria = st.file_uploader('Anexe o primeiro arquivo .txt com as palavras separadas por espaço:', type= ['txt'])
entradaDeTextoSecundaria = st.file_uploader('Anexe o segundo arquivo .txt com as palavras separadas por espaço:', type= ['txt'])

botaoFoiSelecionado = st.button('Faça a mágica', on_click = compararAsEntradas(entradaDeTextoPrimaria, entradaDeTextoSecundaria))

def compararAsEntradas(entradaDeTextoPrimaria, entradaDeTextoSecundaria):
  'Eis os resultado:'
  

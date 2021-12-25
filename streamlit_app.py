import streamlit as st
import pandas as pd

st.title('Tenho vocabulário para isso?')

'Esta aplicação ajuda você a cruzar palavras de duas fontes de entrada e retornar as palavras em comum e diferentes.'

'Casos de uso:'
'\ti) Comparar os vocabulários ensinado e de uma música para aulas de inglês;'
'\tii) Encontrar palavras desconhecidas em um texto;'
'\tiii) Antecipar o vocabulário necessário para um filme.'

st.subheader('Use o app!')
'Anexe os arquivos com as palavras separadas por linhas:'
entradaDeTextoPrimaria = st.file_uploader('Primeiro arquivo:', type= ['csv', 'txt'])
entradaDeTextoSecundaria = st.file_uploader('Segundo arquivo:', type= ['csv', 'txt'])

botaoFoiSelecionado = st.button('Faça a mágica')

if botaoFoiSelecionado:
  if not(entradaDeTextoPrimaria and entradaDeTextoSecundaria):
    'Anexe os dois arquivos!'
  else:
    dataframePrimaria = pd.read_csv(entradaDeTextoPrimaria, header = None, engine = 'python')
    dataframeSecundaria = pd.read_csv(entradaDeTextoSecundaria, header = None, engine = 'python')
    
    if (dataframePrimaria.shape[1]  > 1) or (dataframeSecundaria.shape[1] > 1):
      'As palavras devem ser separadas em diferentes linhas. Por exemplo:'
      st.table(pd.DataFrame(data = {'': ['casa', 'lar', 'prédio']}))
    
    else:    
      'As palavras do segundo arquivo que estão presentes no primeiro:'
      dfComPalavrasComuns = dataframePrimaria.compare(dataframeSecundaria, align_axis = 1, keep_equal = True)
      dfComPalavrasComuns

      'As palavras do segundo arquivo que são diferentes do primeiro:'
      dfComPalavrasDiferentes = dataframePrimaria.compare(dataframeSecundaria, align_axis = 1)
      dfComPalavrasDiferentes

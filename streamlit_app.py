import streamlit as st
import pandas as pd
import numpy as np

st.title('Tenho vocabulário para isso?')

'Esta aplicação ajuda você a cruzar palavras de duas fontes de entrada e retornar as palavras em comum e diferentes.'

'Casos de uso:'
'\ti) Comparar os vocabulários ensinado e de uma música para aulas de inglês;'
'\tii) Encontrar palavras desconhecidas em um texto;'
'\tiii) Antecipar o vocabulário necessário para um filme.'

st.subheader('Use o app!')
'Anexe os arquivos com as palavras separadas por linhas:'
entradaDeTextoPrimaria = st.file_uploader('Primeiro arquivo:', type= ['txt'])
entradaDeTextoSecundaria = st.file_uploader('Segundo arquivo:', type= ['txt'])

botaoFoiSelecionado = st.button('Faça a mágica')

if botaoFoiSelecionado:
  if not(entradaDeTextoPrimaria and entradaDeTextoSecundaria):
    'Anexe os dois arquivos!'
  else:
    dataframePrimaria = pd.read_csv(entradaDeTextoPrimaria, header = None).stack()
    dataframeSecundaria = pd.read_csv(entradaDeTextoSecundaria, header = None).stack()
    numpyPrimaria = dataframePrimaria.to_numpy()
    numpySecundaria = dataframeSecundaria.to_numpy()
    
    while True:
      for posicao, conteudo in np.ndenumerate(numpyPrimaria):
        palavrasDeConteudo = conteudo.split(' ')
        if len(palavrasDeConteudo) > 1:
          numpyPrimaria = np.delete(numpyPrimaria, posicao)
          numpyPrimaria = np.append(numpyPrimaria, palavrasDeConteudo)
          break
      if posicao[0] == len(numpyPrimaria) - 1:
        break
    
    while True:
      for posicao, conteudo in np.ndenumerate(numpySecundaria):
        palavrasDeConteudo = conteudo.split(' ')
        if len(palavrasDeConteudo) > 1:
          numpySecundaria = np.delete(numpySecundaria, posicao)
          numpySecundaria = np.append(numpySecundaria, palavrasDeConteudo)
          break
      if posicao[0] == len(numpySecundaria) - 1:
        break
    
    for posicao, conteudo in np.ndenumerate(numpyPrimaria):
      if conteudo == '':
        numpyPrimaria = np.delete(numpyPrimaria, posicao)
      else:
        conteudo
        for carac in conteudo:
          if carac in '''!()[]{};:'"\,<>./?@#$%^&*_~''':
            conteudo = conteudo.replace(carac, '')
            conteudo
        numpyPrimaria[posicao] = conteudo
        
    #for posicao, conteudo in np.ndenumerate(numpySecundaria):
    #  if conteudo == '':
    #    numpySecundaria = np.delete(numpySecundaria, posicao) 
    #  else:
    #    for carac in conteudo:
    #      if carac in '''!()[]{};:'"\,<>./?@#$%^&*_~''':
    #        conteudo = conteudo.replace(carac, '')
    #    numpySecundaria[posicao] = conteudo  
    
    numpyPrimaria
    numpySecundaria

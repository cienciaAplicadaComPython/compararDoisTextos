import streamlit as st
import pandas as pd
import numpy as np

#---------------------------------------------------------------------
#Função para comparar as entradas de texto
#@st.cache
def compararArquivos(entradaDeTextoPrimariaPorArquivo, entradaDeTextoPrimariaNoNavegador, entradaDeTextoSecundariaPorArquivo, entradaDeTextoSecundariaNoNavegador):
  #---------------------------------------------------------------------
  #Caso nenhuma ou somente uma entrada seja enviada
  if not((entradaDeTextoPrimariaPorArquivo or entradaDeTextoPrimariaNoNavegador) and (entradaDeTextoSecundariaPorArquivo or entradaDeTextoSecundariaNoNavegador)):
    'Uma ou as duas entradas estão faltando!'
  #---------------------------------------------------------------------

  #---------------------------------------------------------------------
  #Caso duas primeiras ou segundas entradas existam:
  elif (entradaDeTextoPrimariaPorArquivo and entradaDeTextoPrimariaNoNavegador) or (entradaDeTextoSecundariaPorArquivo and entradaDeTextoSecundariaNoNavegador):
    'Existem duas primeiras ou segundas entradas!'
  #---------------------------------------------------------------------

  #---------------------------------------------------------------------
  #Caso duas entradas sejam enviadas 
  else:
    #---------------------------------------------------------------------
    #Se houve envio de arquivos 
    if entradaDeTextoPrimariaPorArquivo:
      dataframePrimaria = pd.read_csv(entradaDeTextoPrimariaPorArquivo, header = None).stack()
      numpyPrimaria = dataframePrimaria.to_numpy()
      #---------------------------------------------------------------------
      #Separa o arquivo em palavras de acordo com os espaços
      while True:
        for posicao, conteudo in np.ndenumerate(numpyPrimaria):
          palavrasDeConteudo = conteudo.split(' ')
          if len(palavrasDeConteudo) > 1:
            numpyPrimaria = np.delete(numpyPrimaria, posicao)
            numpyPrimaria = np.append(numpyPrimaria, palavrasDeConteudo)
            break
        if posicao[0] == len(numpyPrimaria) - 1:
          break
      #---------------------------------------------------------------------
    #---------------------------------------------------------------------

    if entradaDeTextoSecundariaPorArquivo:
      dataframeSecundaria = pd.read_csv(entradaDeTextoSecundariaPorArquivo, header = None).stack()
      numpySecundaria = dataframeSecundaria.to_numpy()
      #---------------------------------------------------------------------
      #Separa o arquivo em palavras de acordo com os espaços
      while True:
        for posicao, conteudo in np.ndenumerate(numpySecundaria):
          palavrasDeConteudo = conteudo.split(' ')
          if len(palavrasDeConteudo) > 1:
            numpySecundaria = np.delete(numpySecundaria, posicao)
            numpySecundaria = np.append(numpySecundaria, palavrasDeConteudo)
            break
        if posicao[0] == len(numpySecundaria) - 1:
          break
      #---------------------------------------------------------------------
    #--------------------------------------------------------------------- 

    #---------------------------------------------------------------------
    #Se os textos foram inseridos diretamente no navegador 
    if entradaDeTextoPrimariaNoNavegador:
      palavrasDaEntradaDeTextoPrimariaNoNavegador = str.split(entradaDeTextoPrimariaNoNavegador)
      numpyPrimaria = np.array(palavrasDaEntradaDeTextoPrimariaNoNavegador)
    if entradaDeTextoSecundariaNoNavegador:
      palavrasDaEntradaDeTextoSecundariaNoNavegador = str.split(entradaDeTextoSecundariaNoNavegador)
      numpySecundaria = np.array(palavrasDaEntradaDeTextoSecundariaNoNavegador)
    #---------------------------------------------------------------------

    #---------------------------------------------------------------------
    #Deleta os índices vazios e as pontuações dos arquivos
    while True:
      for posicao, conteudo in np.ndenumerate(numpyPrimaria):
        if conteudo == '':
          numpyPrimaria = np.delete(numpyPrimaria, posicao)
          break
        else:
          for carac in conteudo:
            if carac in '''!()[]{};:'"\,<>./?@#$%^&*_~''':
              conteudo = conteudo.replace(carac, '')
          numpyPrimaria[posicao] = conteudo
      if posicao[0] == len(numpyPrimaria) - 1:
        break

    while True:
      for posicao, conteudo in np.ndenumerate(numpySecundaria):
        if conteudo == '':
          numpySecundaria = np.delete(numpySecundaria, posicao) 
          break
        else:
          for carac in conteudo:
            if carac in '''!()[]{};:'"\,<>./?@#$%^&*_~''':
              conteudo = conteudo.replace(carac, '')
          numpySecundaria[posicao] = conteudo
      if posicao[0] == len(numpySecundaria) - 1:
        break
    #---------------------------------------------------------------------

    #---------------------------------------------------------------------
    #Deleta as palavras repetidas
    numpyPrimaria = np.unique(numpyPrimaria)
    numpySecundaria = np.unique(numpySecundaria)
    #---------------------------------------------------------------------

    #---------------------------------------------------------------------
    # Salva as palavras comuns e diferentes um duas listas
    palavrasComuns = []
    palavrasDiferentes = []
    for _, palavraDoArquivo2 in np.ndenumerate(numpySecundaria):
      if np.any(numpyPrimaria == palavraDoArquivo2):
        palavrasComuns.append(palavraDoArquivo2)
      else:
        palavrasDiferentes.append(palavraDoArquivo2)
     #---------------------------------------------------------------------

    #---------------------------------------------------------------------
    #Expõe os resultados
    'As seguintes palavras estão no primeiro e segundo arquivos:'
    dataFrameDePalavrasComuns = pd.DataFrame(palavrasComuns, index = range(1, len(palavrasComuns) + 1), columns = ['Palavras Comuns'])
    st.table(dataFrameDePalavrasComuns)

    'As seguintes palavras estão somente no segundo arquivo:'
    dataFrameDePalavrasDiferentes = pd.DataFrame(palavrasDiferentes, index = range(1, len(palavrasDiferentes) + 1), columns = ['Palavras Diferentes'])
    st.table(dataFrameDePalavrasDiferentes)
    #---------------------------------------------------------------------

    'Algumas palavras podem ser mescladas durante a leitura dos arquivos devido à pontuação. Por exemplo:'
    'i) station/hardware'
    'ii) exemplo:água'
    'Experimente escrever a pontuação entre espaços e tente novamente.'

    #---------------------------------------------------------------------
    #Baixa os arquivos TXT dos resultados
    st.download_button('Baixe as palavras comuns', data = dataFrameDePalavrasComuns.to_csv().encode('ISO-8859-1'), file_name = 'palavrasComuns.csv', mime = 'text/csv')
    st.download_button('Baixe as palavras diferentes', data = dataFrameDePalavrasDiferentes.to_csv().encode('ISO-8859-1'), file_name = 'palavrasDiferentes.csv', mime = 'text/csv')
    #---------------------------------------------------------------------
#---------------------------------------------------------------------

st.title('Comparar Dois Textos')

'Esta aplicação ajuda você a cruzar as palavras de duas fontes de entrada e retornar as palavras em comum e diferentes.'

st.subheader('Onde utilizar?')
'\t I) Comparar os vocabulários ensinado e de uma música para aulas de inglês;'
'\t II) Visualizar as palavras diferentes entre dois discursos;'
'\t III) Antecipar o vocabulário necessário para um filme;'
'\t IV) Identificar as palavras comuns entre dois diálogos.'

st.subheader('Como utilizar?')
'Faça o upload de dois arquivos de texto *TXT* com os vocabulários, discursos, diálogos e outros para comparação ou digite-os no navegador e aperte o botão **Comparar arquivos**.'

st.subheader('Use o app!')
'Anexe os arquivos:'
#---------------------------------------------------------------------
#Recebe arquivos por upload
entradaDeTextoPrimariaPorArquivo = st.file_uploader('Primeiro arquivo:', type= ['txt'])
entradaDeTextoSecundariaPorArquivo = st.file_uploader('Segundo arquivo:', type= ['txt'])
#---------------------------------------------------------------------

'Ou digite os textos:'
#---------------------------------------------------------------------
#Recebe os textos diretamente no navegador
entradaDeTextoPrimariaNoNavegador = st.text_area('Primeiro texto:')
entradaDeTextoSecundariaNoNavegador = st.text_area('Segundo texto:')
#---------------------------------------------------------------------

botaoFoiSelecionado = st.button('Comparar arquivos')
if botaoFoiSelecionado:
  compararArquivos(entradaDeTextoPrimariaPorArquivo, entradaDeTextoPrimariaNoNavegador, entradaDeTextoSecundariaPorArquivo, entradaDeTextoSecundariaNoNavegador)

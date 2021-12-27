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
'Anexe os arquivos:'
#---------------------------------------------------------------------
#Recebe arquivos por upload
entradaDeTextoPrimariaPorArquivo = st.file_uploader('Primeiro arquivo:', type= ['txt'])
entradaDeTextoSecundariaPorArquivo = st.file_uploader('Segundo arquivo:', type= ['txt'])
#---------------------------------------------------------------------

'Ou digite as palavras:'
#---------------------------------------------------------------------
#Recebe o texto no navegador 
entradaDeTextoPrimariaPeloNavegador = st.text_area('Digite o primeiro texto:')
entradaDeTextoSecundariaPeloNavegador = st.text_area('Digite o segundo texto:')
#---------------------------------------------------------------------

botaoFoiSelecionado = st.button('Comparar arquivos')

if botaoFoiSelecionado:
  #---------------------------------------------------------------------
  #Caso nenhuma ou somente uma entrada seja enviada
  if not((entradaDeTextoPrimariaPorArquivo or entradaDeTextoPrimariaPeloNavegador) and (entradaDeTextoSecundariaPorArquivo or entradaDeTextoSecundariaPeloNavegador)):
    'Anexe os dois arquivos ou digite as palavras!'
  #---------------------------------------------------------------------
  
  #---------------------------------------------------------------------
  #Caso duas entradas sejam enviadas 
  else:
    #---------------------------------------------------------------------
    #Checa arquivos anexados
    if entradaDeTextoPrimariaPorArquivo:
      dataframePrimaria = pd.read_csv(entradaDeTextoPrimariaPorArquivo, header = None).stack()
      numpyPrimaria = dataframePrimaria.to_numpy()
    if entradaDeTextoSecundariaPorArquivo:
      dataframeSecundaria = pd.read_csv(entradaDeTextoSecundariaPorArquivo, header = None).stack()
      numpySecundaria = dataframeSecundaria.to_numpy()
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #Checa palavras digitadas no navegador
    if entradaDeTextoPrimariaPeloNavegador:
      numpyPrimaria = np.fromstring(entradaDeTextoPrimariaPeloNavegador, sep=',')
    if entradaDeTextoSecundariaPeloNavegador:
      numpySecundaria = np.fromstring(entradaDeTextoSecundariaPeloNavegador, sep=',')
    #---------------------------------------------------------------------
    
    #---------------------------------------------------------------------
    #Separa os arquivos em palavras de acordo com os espaços
    len(numpyPrimaria)
    len(numpySecundaria)
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
    st.table(pd.DataFrame(palavrasComuns, index = range(1, len(palavrasComuns) + 1), columns = ['Palavras Comuns']))
    
    'As seguintes palavras estão somente no segundo arquivo:'
    st.table(pd.DataFrame(palavrasDiferentes, index = range(1, len(palavrasDiferentes) + 1), columns = ['Palavras Diferentes']))
    #---------------------------------------------------------------------
    
    'Algumas palavras podem ser mescladas durante a leitura dos arquivos devido à pontuação. Por exemplo:'
    'i) station/hardware'
    'ii) exemplo:água'
    'Experimente escrever a pontuação entre espaços e enviar os arquivos novamente.'
  #---------------------------------------------------------------------
 
    
        

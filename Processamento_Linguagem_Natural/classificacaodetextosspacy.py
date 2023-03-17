# -*- coding: utf-8 -*-
"""ClassificacaoDeTextosSpacy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EQ0Z7slSa8wNhhpa1TFFOHI3F1M3cYIK
"""

!pip install spacy --upgrade
!pip install -q spacy==2.2.3 #Atualizado: 02/05/2021 Obs: utilizar esta versão.

!python3 -m spacy download pt

import pandas as pd
import string
import spacy
import random
import seaborn as sns
import numpy as np

base_dados = pd.read_csv('/content/base_treinamento.txt', encoding = 'utf-8')

base_dados.shape

base_dados.head()

base_dados.tail()

sns.countplot(base_dados['emocao'], label = 'Contagem');

pontuacoes = string.punctuation
pontuacoes

from spacy.lang.pt.stop_words import STOP_WORDS
stop_words = STOP_WORDS
print(stop_words)
len(stop_words)

pln = spacy.load('pt_core_news_sm')
pln

def preprocessamento(texto):
  texto = texto.lower()
  documento = pln(texto)

  lista = []
  for token in documento:
    #lista.append(token.text)
    lista.append(token.lemma_)

  lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in pontuacoes]
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

  return lista

texto_teste = '@behin_d_curtain :D Para :( mim, http://www.iaexpert.com.br é precisamente o contrário :) Vem a chuva e vem a boa disposição :)'
resultado = preprocessamento(texto_teste)
resultado

base_dados.head(10)

base_dados['texto'] = base_dados['texto'].apply(preprocessamento)
base_dados.head(10)

exemplo_base_dados = [["este trabalho é agradável", {"ALEGRIA": True, "MEDO": False}],
                      ["este lugar continua assustador", {"ALEGRIA": False, "MEDO": True}]]

type(exemplo_base_dados)

exemplo_base_dados[0]

base_dados_final = []
for texto, emocao in zip(base_dados['texto'], base_dados['emocao']):
  #print(texto, emocao)
  if emocao == 'alegria':
    dic = ({'ALEGRIA': True, 'MEDO': False})
  elif emocao == 'medo':
    dic = ({'ALEGRIA': False, 'MEDO': True})
  
  base_dados_final.append([texto, dic.copy()])

len(base_dados_final)

base_dados_final[0]

base_dados_final[0][0]

base_dados_final[0][1]

type(base_dados_final[0][1])

base_dados_final

modelo = spacy.blank('pt')
categorias = modelo.add_pipe("textcat")
categorias.add_label("ALEGRIA")
categorias.add_label("MEDO")
historico = []

from spacy.training.example import Example

modelo.begin_training()
for epoca in range(1000):
    random.shuffle(base_dados_final)
    losses = {}
    exemplos = []
    for texto, entities in base_dados_final:
        doc = modelo.make_doc(texto)
        exemplo = Example.from_dict(doc, {"cats": entities})
        exemplos.append(exemplo)
    modelo.update(exemplos, losses=losses)
    if epoca % 100 == 0:
        print(losses)
        historico.append(losses)

historico_loss = []
for i in historico:
  historico_loss.append(i.get('textcat'))

historico_loss = np.array(historico_loss)
historico_loss

import matplotlib.pyplot as plt
plt.plot(historico_loss)
plt.title('Progressão do erro')
plt.xlabel("Épocas")
plt.ylabel("Erro")

modelo.to_disk("modelo")






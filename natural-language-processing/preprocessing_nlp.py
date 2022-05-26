# -*- coding: utf-8 -*-
"""lista2-pln.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xGjP8g7ADDymLr-f82aUtcJJ_d1zjEIg

[**tweets.csv**](https://gist.github.com/yrribeiro/48c8cdb33c2c552d86f36e8ead6f42c2), dataset used in this exercise.
"""

import re
import string
import pandas as pd
import numpy as np
import seaborn as sns
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.stem.lancaster import LancasterStemmer

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')                  DESCOMENTE ANTES DE RODAR PELA PRIMEIRA VEZ

dataset = 'tweets.csv'

"""**Questão 1**: *Determine a distribuição de comprimentos dos textos (em quantidade de caracteres), listando estas quantidades e plotando um histograma.*"""

df = pd.read_csv(dataset)
txt_column = df['text']
print(f'Size: {df.shape}\nColumns: {list(df.columns)}')

each_txt_length = np.array([len(txt_length) for txt_length in txt_column])
each_txt_length

histogram = sns.histplot(each_txt_length,
             stat='count', 
             color='navy', 
             binwidth=10,
             alpha = 0.5,
             kde = True
            ).set(title='Frequency of tweets size (in characters)', xlabel='Number of characters')

"""**Questão 2**: *Remova todas as palavras que contêm números; Converta as palavras para minúsculas; Remova pontuação; Tokenize os textos em palavras, gerando um dicionário  único com **n** tokens e convertendo cada texto em um vetor de dimensão **n** com a respectiva contagem de palavras. Em seguida, encontre as palavras mais frequentes da base de textos.*"""

# remove urls
rex_pattern = r'http[s]?://([\w\.]+)\/([\w]+)' 
replacer = lambda x: re.sub(rex_pattern, '', x)
txt_column = list(map(replacer, txt_column))
txt_column

# remove number
rex_pattern = r'[\d+]' 
replacer = lambda x: re.sub(rex_pattern, '', x)
txt_column = list(map(replacer, txt_column))

txt_column

# remove punctuation and emojis
rex_pattern = r'[^\w\s]+'
replacer = lambda x: re.sub(rex_pattern, '', x)
txt_column = list(map(replacer, txt_column))
txt_column

# transform to lowercase and tokenize
all_tokens = []
i = 0
for tokens in txt_column:
  txt_column[i] = tokens.lower()
  all_tokens += word_tokenize(txt_column[i])
  i = i+1
len(all_tokens)

txt_column

cv = CountVectorizer()
X = cv.fit_transform(txt_column)
# print(cv.get_feature_names())
array = X.toarray()
X.toarray()

summ = np.sum(array, axis=0)
# print(summ)
sorted_arr_index = np.argsort(summ)
# print(sorted_arr_index)
n = len(sorted_arr_index)
how_many_words = sorted_arr_index[n:n-6:-1]
# print(how_many_words)
i = 1
for index in how_many_words:
  print(f'{i}° mais frequente: {cv.get_feature_names()[index]} (Repetida {summ[index]} vezes)')
  i = i+1

"""**Questão 3**: *Remova stopwords; Realize rotulação de POS; Realize stemização; Exiba os resultados em alguns textos. Verifique quais são as palavras mais frequentes e compare com as palavras mais frequentes da questão anterior.*"""

# remove stopwords
cv = CountVectorizer(stop_words='english')
no_stopwords_array = cv.fit_transform(txt_column).toarray()
# pd.DataFrame(no_stopwords_array, columns=cv.get_feature_names())

summ = np.sum(no_stopwords_array, axis=0)
sorted_arr_index = np.argsort(summ)
n = len(sorted_arr_index)
how_many_words = sorted_arr_index[n:n-6:-1]
i = 1
for index in how_many_words:
  print(f'{i}° mais frequente: {cv.get_feature_names()[index]} (Repetida {summ[index]} vezes)')
  i = i+1

Assim, conseguimos entender o porquê da necessidade de remoção de stopwords. Elas interferem no estudo do resultado, uma vez 
que é normal em uma linguagem a frequência de artigos e advérbios ser muito maior.

# pos tagging
text_sample = [txt_column[sentence] for sentence in range(70,75)]
i = 0
for sentence in text_sample:
  tokens = pos_tag(word_tokenize(sentence))
  print(f'\n{i+1}° exemplo:\nTexto: "{text_sample[i]}"\nPOS Tag: {tokens}')
  i = i + 1

# stemming
stemmer = LancasterStemmer()
text_sample = [txt_column[sentence] for sentence in range(0,5)]
for sentence in text_sample:
  print(f'\nSENTENCE: {sentence}')
  for word in word_tokenize(sentence):
    print(stemmer.stem(word))
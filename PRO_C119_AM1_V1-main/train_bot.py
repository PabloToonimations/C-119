# Bibliotecas de preprocesamiento de datos de texto
import nltk

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

words = []
classes = []
word_tags_list = []
ignore_words = ['?','!',',','.',"'s","'m"]
train_data_file = open ('intents.json').read()
intents = json.loads(train_data_file)

# Función para añadir palabras raíz (steam words)
def get_stem_words(words,ignore_words):
    stem_words = []
    for word in words:
        if word not in ignore_words:
            w = stemmer.stem(word.lower())
            stem_words.append(w)
    return stem_words

for intent in intents ["intents"]:


    
        # Agregar todas las palabras de patrones a una lista
        
        # Agregar todas las etiquetas a la lista de clases
         

# Crear un corpus de palabras para el chatbot


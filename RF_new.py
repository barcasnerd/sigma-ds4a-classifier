#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# In[7]:


def model_classifier(loc):
    """Función para entrar algoritmo de Random Forest
    loc = Localización de datos
    return:
    
    model: Clasificador entrenado"""
    
    # Importar datos
    df = pd.read_csv(loc, encoding = 'latin-1' )
    df.columns = ['tik_codigo', 'descripcion', 'propietario', 'categoria', 'ans',
       'nombre_cliente', 'Linea_Negocio', 'newCategory', 'newDescription']

    df.dropna(subset = ["newDescription", "newCategory"], inplace=True)
    df = df.reset_index(drop=True)
    documents = df[["newDescription", "newCategory"]].copy()

    # Creación de variables dependientes e independientes

    X = documents.newDescription
    y = documents.newCategory
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 19)

    # Transformar los datos de texto apoyados en Tf-Idf

    tfidf_vectorizer = TfidfVectorizer(use_idf=True)
    X_train = tfidf_vectorizer.fit_transform(X_train) 
    X_test = tfidf_vectorizer.transform(X_test)
    
    classifier = RandomForestClassifier(max_features='sqrt', n_estimators=1000)
    classifier.fit(X_train, y_train)
   
    return classifier


# In[4]:


def transform_data(loc, data):
    """Función para transformar datos. Debe ser un arreglo iterable
    
    loc: Localización del documento
    data: Nuevas observaciones"""
    
        # Importar datos
    df = pd.read_csv(loc, encoding = 'latin-1' )
    df.columns = ['tik_codigo', 'descripcion', 'propietario', 'categoria', 'ans',
       'nombre_cliente', 'Linea_Negocio', 'newCategory', 'newDescription']

    df.dropna(subset = ["newDescription", "newCategory"], inplace=True)
    df = df.reset_index(drop=True)
    documents = df[["newDescription", "newCategory"]].copy()

    # Creación de variables dependientes e independientes

    X = documents.newDescription
    y = documents.newCategory
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 19)
    
    vectorizer = TfidfVectorizer(use_idf=True)
    vectorizer.fit(X_train)
    data = vectorizer.transform(data)
    return data    


# In[20]:


def make_pred(loc, new_data, classifier):
    """Función para realizar pronósticos
    
    loc = Localización del del archivo con los datos a analizar
    new_data = Nuevos datos a pronósticar
    classifier = modelo clasificador entrenado"""
    
    categories = ['Nuevo requerimiento', 'Servicios', 'Datos', 'Visor', 'GPS','Funcionalidad', 'Formulario',
                  'Reporte', 'Sistema', 'Consultas','App', 'Otros', 'Shape']   
    
    data = transform_data(loc, new_data)
    category = classifier.predict(data)
    probabilities = classifier.predict_proba(data)
    cat_prob = pd.DataFrame(probabilities,columns=categories).T
    cat_prob.columns = ["Category probability"]*len(cat_prob.columns)
    cat_prob = cat_prob.sort_values("Category probability", axis=0, ascending=False).head(3)
    
    return cat_prob


import streamlit as st
import pandas as pd
import sklearn
import joblib

sepal_length = st.text_input("sepal_length :", "")
sepal_width = st.text_input("sepal_width :", "")
petal_length = st.text_input("petal_length :", "")
petal_width = st.text_input("petal_width :", "")
model = joblib.load("modelIRIS.pkl")

if (sepal_length and sepal_width and petal_length and petal_width) :
    irisX = pd.DataFrame({
    'sepal_length': [float(sepal_length)],
    'sepal_width': [float(sepal_width)],
    'petal_length': [float(petal_length)],
    'petal_width': [float(petal_width)]
    })
    Y_pred = model.predict_proba(irisX)[0]
    
    if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
        st.text("setosa")
    elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
        st.text("versicolor")
    else :
        st.text("virginica")
    
    
else :
    st.text("Remplis tous les champs")
    
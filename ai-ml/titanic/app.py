import streamlit as st
import sys
sys.path.append("C:/Users/adity/miniconda3/envs/py310/Lib/site-packages/numpy/_utils")

from utils import columns, PrepProcesor

import numpy as np
import pandas as pd
import joblib

model = joblib.load('C:/Users/adity/OneDrive/Downloads/xgbpipe.joblib')
st.title('Did they survive? :ship:')
df = pd.read_csv('train.csv')
df.dropna(axis=1, inplace=True)
# PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
passengerid = st.text_input("Input Passenger ID", '123456') 
pclass = st.selectbox("Choose class", [1,2,3])
name  = st.text_input("Input Passenger Name", 'John Smith')
sex = st.select_slider("Choose sex", ['male','female'])
age = st.slider("Choose age",0,100)
sibsp = st.slider("Choose siblings",0,10)
parch = st.slider("Choose parch",0,2)
ticket = st.text_input("Input Ticket Number", "12345") 
fare = st.number_input("Input Fare Price", 0,1000)
cabin = st.text_input("Input Cabin", "C52") 
embarked = st.select_slider("Did they Embark?", ['S','C','Q'])

def predict(): 
    row = np.array([passengerid,pclass,name,sex,age,sibsp,parch,ticket,fare,cabin,embarked]) 
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)[0]
   
    print("hsudfhsd")
    if prediction[0] == 1: 
        st.success('Passenger Survived :thumbsup:')
        print("hi")
    else: 
        st.error('Passenger did not Survive :thumbsdown:') 
        print("hi")
    

trigger = st.button('Predict', on_click=predict)
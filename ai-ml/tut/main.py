import pandas as pd
import numpy as np
from sklearn import linear_model
import math
import streamlit as st
import pickle

df = pd.read_csv('data.csv')
median_bedrooms = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(median_bedrooms)
st.header('Predict House Price')
age = st.slider('Age', 1, 100)
bedrooms = st.number_input('Bedrooms', 1, 10)
square = st.number_input('Square Feet', 1, 100000)

reg = linear_model.LinearRegression()

reg.fit(df[['area', 'bedrooms', 'age']].values, df.price)

with open('model_pickle.pkl', 'wb')as f:
    pickle.dump(reg,f)

s = st.button('Predict')
picklein = open('model_pickle.pkl', 'rb')
prediction = pickle.load(picklein)

if s:
    st.text(prediction.predict([[age,bedrooms,square]]))





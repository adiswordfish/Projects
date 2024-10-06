import pandas as pd
import numpy as np
from sklearn import linear_model
import math
import streamlit as st
st.header("Predic House Prices (US)")
df = pd.read_csv('Housing.csv')
a=st.number_input('Area', 1, 1000000)
b=st.slider('Bedrooms', 1, 100)
c=st.slider('Bathrooms', 1,100)
d=st.slider('Floors', 1,200)

df.drop(['mainroad', 'guestroom', 'basement'], inplace=True, axis=1) 

reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'bathrooms', 'stories']].values, df.price )

p =  reg.predict([[a,b,c,d]])
p
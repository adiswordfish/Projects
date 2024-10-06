import pandas as pd
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
df = pd.read_csv("insurance.csv")
X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance, test_size=0.1)
model = LogisticRegression()
model.fit(X_train, y_train)
st.header("Will you buy insurance?")
st.text("0 = No\n1 = Yes")
age = st.slider('Age', 16, 100)

predict = model.predict([[age]])
predict

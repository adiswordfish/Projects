import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import streamlit as st
df = pd.read_csv("salaries.csv")
jobs = ["Google", "abc pharma", "facebook"]
roles = ["sales executive", "business manager", "computer programmer"]
degree = ["bachelors", "masters"]
st.header("More Than 100K Salary")
st.text("This is made up\n 0 = Less than 100k\n 1 = More than 100k")
a = st.selectbox('Company', options=jobs)
b = st.selectbox('Role', options=roles)
c = st.selectbox('Degree', options=degree)
inputs = df.drop('salary_more_then_100k', axis='columns')
target = df['salary_more_then_100k']
le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()
inputs['company_n'] = le_company.fit_transform(inputs['company'])
inputs['job_n'] = le_job.fit_transform(inputs['job'])
inputs['degree_n'] = le_degree.fit_transform(inputs['degree'])
model = tree.DecisionTreeClassifier()
inputs_n = inputs.drop(['company', 'job', 'degree'], axis='columns')
model.fit(inputs_n, target)

if a == 'Google':
    d = 2
elif a == 'abc pharma':
    d = 0
else:
    d=1

if b == 'sales executive':
    e = 2
elif b == 'business manager':
    e = 0
else:
    e=1

if c == 'bachelors':
    f = 0
else:
    f = 1


predict = model.predict([[d,e,f]])
predict
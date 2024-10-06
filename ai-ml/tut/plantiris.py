# %%
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
iris = load_iris()

# %%
dir(iris)

# %%
st.title('Which type of plant?')
st.text(' 0 = Setosa\n 1 = Versicolor\n 2 = Virginica')

# %%
df = pd.DataFrame(iris.data,  columns=iris.feature_names)


# %%
df['target'] = iris.target

# %%


# %%
df[df.target==1].head()

# %%
df['flower_name'] = df.target.apply(lambda x: iris.target_names[x])

# %%


# %%


# %%


# %%


# %%


# %%
import matplotlib.pyplot as plt

df0 = df[df.target==0]
df1 = df[df.target==1]
df2 = df[df.target==2]

# %%


# %%
# %%
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'],color="green",marker='+')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'],color="blue",marker='.')

# %%
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'],color="green",marker='+')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'],color="blue",marker='.')

# %%

from sklearn.model_selection import train_test_split

# %%
X = df.drop(['target','flower_name'], axis='columns')
y = df.target

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# %%

from sklearn.svm import SVC
model = SVC()

# %%

model.fit(X_train, y_train)

# %%
a = st.number_input('Sepal Length (CM)', 1, 10000)
b = st.number_input('Sepal Width (CM)', 1, 10000)
c = st.number_input('Petal Length (CM)', 1, 10000)
d = st.number_input('Petal Width (CM)', 1, 10000)


# %%

a = model.predict([[a,b,c,d]])
a

# %%




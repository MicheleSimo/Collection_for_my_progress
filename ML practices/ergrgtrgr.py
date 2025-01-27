import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

data = pd.DataFrame(data={
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [1.5, 1.7, 2.5, 3.5, 3.8, 4.5, 5.5, 6.5, 7.5, 8.5]
})
print(data['X'])
print(data[['X']])

iris = pd.load_iris()
dfIris = pd.DataFrame(data=iris)
dfIris['target'] = iris.target
X = dfIris.drop('target',axis=1)
y = dfIris['target']
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=40)
#Creazione e gestione modello scelto
model = DecisionTreeClassifier(random_state=40)
model.fit(x_train,y_train)
ypred = model.predict(x_test)
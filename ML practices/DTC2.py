from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.DataFrame(data={
    "first" : [9,40,100],
    "second" : [20,30,100],
    "y" : [10,4,10]
})
X = df.drop("y",axis=1)
y = df["y"]
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
model = DecisionTreeClassifier(max_depth=2,random_state=40)
model.fit(x_train,y_train)
ypred = model.predict(x_test)
print(accuracy_score(ypred,y_test))
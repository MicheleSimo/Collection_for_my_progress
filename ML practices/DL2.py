import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler

X,y = make_classification(n_samples=100,n_features=10,n_classes=2)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4)
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

model = Sequential()
model.add(Dense(64,activation="relu",input_dim=8))
model.add(Dense(32,activation="relu"))
model.add(Dense(1,activation="sigmoid"))
model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
model.fit(X_train,y_train,epochs=30,batch_size=3)
loss,accuracy = model.evaluate(X_test,y_test)
predicted = model.predict(X_test)
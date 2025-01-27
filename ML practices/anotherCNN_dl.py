import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import mnist
from keras import backend as K
from sklearn.model_selection import GridSearchCV
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

(x_train,y_train) , (x_test,y_test) = mnist.load_data()

# Imposta le dimensioni delle immagini
img_rows, img_cols = 28, 28

# Controlla il formato dei dati
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

#Creazione modello

def create_model(optimizer='adam'):
    model = Sequential()
    model.add(layers.Conv2D(32,(3,3),activation="relu",input_shape=input_shape))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(64,(3,3),activation="relu"))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Conv2D(128,(3,3),activation="relu"))
    model.add(layers.MaxPooling2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(128,activation="relu"))
    model.add(layers.Dense(1,activation="sigmoid"))
    model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])
    return model

#Training, compile e valutazione modello
model = KerasClassifier(build_fn=create_model, verbose=0)
param_grid = {
    'batch_size': [10, 20],
    'epochs': [10, 50],
    'optimizer': ['SGD', 'Adam']
}
grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
#model.fit(x_train,y_train,epochs=30,batch_size=5)
grid_result = grid.fit(x_train,y_train)
loss, acc = model.evaluate(x_test,y_test)
print(loss)
print(acc)

print(f'Miglior: {grid_result.best_score_} usando {grid_result.best_params_}')

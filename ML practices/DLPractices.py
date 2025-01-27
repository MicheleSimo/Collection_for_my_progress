import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Creare un dataset di esempio (AND)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])  # Output AND

# Creare il modello
model = Sequential()
model.add(Dense(4, activation='relu', input_dim=2))  # Primo strato nascosto con 4 neuroni
model.add(Dense(1, activation='sigmoid'))             # Strato di output

# Compilare il modello
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Addestrare il modello
model.fit(X, y, epochs=100, verbose=0)

# Fare previsioni
predictions = model.predict(X)
print(predictions)
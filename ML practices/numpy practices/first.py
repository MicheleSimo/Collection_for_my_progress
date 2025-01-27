import numpy as np

first = np.array([1,2,3,4,5])
print(first)
#Tramite un range
intervallo = np.arange(1,11)
print(intervallo)
print(intervallo * 10)
lolle = np.linspace(1,100,8)
print(lolle)
#Array con numeri random
random1 = np.random.randint(0,100, size = 10)
print(random1)
uniform = np.random.rand(8)
print(uniform)
#Gestione numeri random con matrici
print(np.random.randn(4,4))
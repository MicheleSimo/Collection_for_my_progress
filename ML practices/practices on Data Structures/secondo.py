import random

lista = [random.randint(1,101) for _ in range(11)]
print(lista)
l2 = [1,3,5,7,9,11]
l2.insert(10,4)
print(l2)
l2.append(100)
print(l2)
l2.pop()
print(l2)
l2.pop(3)
print(l2)
#Misto con numpy

import numpy as np
np1 = np.arange(1,21).reshape(10,2)
print(np1)
np2 = np.arange(1,16)
np2_0 = np2.tolist()
np2_1 = [random.choice(np2_0) for _ in range(4)]
print(np2_1)
np2_2 = np.array_split(np2,5)
print(np2_2[2])
import numpy as np
import numpy.linalg as la

mat = np.array([[4,5,6],[1,2,3],[7,8,9]])
#Calcolo autovalori e autovettori
valori,vettori = la.eig(mat)
print(valori)
print(vettori)
#Calcolo matrice inversa
inverso = la.inv(mat)
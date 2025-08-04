import numpy as np

arr = np.loadtxt('dati.csv', delimiter = ',', skiprows = 0, dtype = str)
print(arr)
print(arr.shape)
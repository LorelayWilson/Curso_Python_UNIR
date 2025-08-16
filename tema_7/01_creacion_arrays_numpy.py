import numpy as np

#Un array unidimensional con los números del 1 al 10 utilizando array()
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)
#Una matriz de ceros de tamaño 3x3 utilizando zeros()
arr2 = np.zeros((3,3))
print(arr2)

#Un array de unos de tamaño 5 utilizando ones()
arr3 = np.ones(5)
print(arr3)

#Un array de 8 elementos con valores espaciados uniformemente entre 0 y 1 utilizando linspace()
arr4 = np.linspace(0, 1, 8)
print(arr4)

#Un array de 10 elementos con valores espaciados uniformemente entre 2 y 20 utilizando arange()
arr5 = np.arange(2, 21, 2)
print(arr5)

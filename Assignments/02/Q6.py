import numpy as np

matrix = np.random.randint(1, 10, size=(2, 2))

determinant = np.linalg.det(matrix)
inverse = None

if determinant != 0:
    inverse = np.linalg.inv(matrix)

print(matrix ,"\n\n" ,determinant,"\n\n" ,inverse)
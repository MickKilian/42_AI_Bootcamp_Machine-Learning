from matrix import Matrix
from matrix import Vector

# 1. Example of matrix and its shape
m1 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
print(m1.shape)  # Output: (3, 2)

# 2. Transpose of m1
print(m1.T())  # Output: Matrix([[0., 2., 4.], [1., 3., 5.]])
print(m1.T().shape)  # Output: (2, 3)

# 3. Example of another matrix m1 and its transposition
m1 = Matrix([[0., 2., 4.], [1., 3., 5.]])
print(m1.shape)  # Output: (2, 3)
print(m1.T())  # Output: Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]])
print(m1.T().shape)  # Output: (3, 2)

# 4. Example of matrix multiplication (m1 * m2)
m1 = Matrix([[0.0, 1.0, 2.0, 3.0], [0.0, 2.0, 4.0, 6.0]])
m2 = Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0], [6.0, 7.0]])
print(m1 * m2)  # Output: Matrix([[28., 34.], [56., 68.]])

# 5. Example of matrix-vector multiplication
m1 = Matrix([[0.0, 1.0, 2.0], [0.0, 2.0, 4.0]])
v1 = Vector([[1], [2], [3]])
print(m1 * v1)  # Output: Matrix([[8], [16]]) or Vector([[8], [16]])

# 6. Example of column vector with addition
v1 = Vector([[1], [2], [3]])
v2 = Vector([[2], [4], [8]])
print(repr(v1))
print(repr(v2))
print(v1 + v2)  # Output: Vector([[3],[6],[11]])

# 7. Example of row vector with addition
v3 = Vector([[1, 2, 3]])  # Vecteur ligne
v4 = Vector([[2, 4, 8]])  # Vecteur ligne
print(repr(v3))  # Affiche la représentation du vecteur v1
print(v3)  # Affiche la représentation du vecteur v1
print(repr(v4))  # Affiche la représentation du vecteur v2
print(v4)  # Affiche la représentation du vecteur v2
print(v3 + v4)  # Devrait afficher : Vector([[3, 6, 11]]) 

# 8. Example of row vector
v5 = Vector([[2, 4, 8]])
print(repr(v5))

# 9. Example of wrong vector
try:
    v3 = Vector([[1, 2], [3, 4]])
    printf(v3)
except ValueError as e:
    print(f"Error: {e}")

# 10. Example of dot product with line vectors
print(v1.dot(v2))

# 11. Example of dot product with column vectors
print(v3.dot(v4))
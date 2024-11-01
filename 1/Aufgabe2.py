import sympy as sp

# a)

A = sp.Matrix([[-2, 1], [-1, 3], [6, -4]])
b = sp.Matrix([[-2], [1]])

# vector product Ab
Ab = A * b
print("Ab: ", Ab)

# b)

btAt = b.T * A.T
print("btAt: ", btAt)

# c)

A = sp.Matrix([[1, -3, 1], [-1, 4, -2]])
b= sp.Matrix([[2], [1], [1]])
Ab = A * b
print("Ab: ", Ab)
# Result: Ab:  Matrix([[0], [0]])

# Given the result from part c, what can you conclude about the relationship between b andthe rows of A?
# The rows of A are linearly dependent, since the result of the matrix-vector multiplication is the zero vector. This means that the vector b is in the null space of A.
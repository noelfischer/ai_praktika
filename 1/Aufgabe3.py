import sympy as sp
# In the following tasks calculate the matrix product AB for the given matrices A, B.
# a)

A = sp.Matrix([[2, -4], [1, 3]])
B = sp.Matrix([[-1, 5], [-3, 1]])
AB = A * B
print("AB: ", AB)

# b)

A = sp.Matrix([[1, 8, -3], [5, -4, 10]])
B = sp.Matrix([[2, -2], [4, 6], [7, -1]])
AB = A * B
print("AB: ", AB)

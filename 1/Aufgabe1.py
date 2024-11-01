import sympy as sp

# a)

a = sp.Matrix([[7], [-4], [2]])
b = sp.Matrix([[3], [-1], [-1]])

# Dot product
dot_product = a.dot(b)
print("Dot product: ", dot_product)

# b)

# Given dot products
dot_ab = 3
dot_ac = -5

# Calculate a · (3b + c)
dot_a_3b_c = 3 * dot_ab + dot_ac
print("a · (3b + c): ", dot_a_3b_c)
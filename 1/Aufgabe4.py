import sympy as sp


# a)

# Define the variables
x1, x2, x3 = sp.symbols('x1 x2 x3')

# Define the function f(x)
f_x = x1**2 + 2*x2**3 - 3*x3 - x1*x2*x3

# Compute the gradient (partial derivatives)
gradient_f_x = [sp.diff(f_x, var) for var in (x1, x2, x3)]

# Display the gradient
print("Gradient of f(x) = ", gradient_f_x)


# b)

# Define the vector components and fixed vector 'a'
x1, x2 = sp.symbols('x1 x2')
a1, a2 = sp.symbols('a1 a2')

# Define the vectors x and a
x = sp.Matrix([x1, x2])
a = sp.Matrix([a1, a2])

# Define the function f(x) = a^T x + x^T x
f_x = a.dot(x) + x.dot(x)

# Compute the derivative of f(x) with respect to x
gradient_f_x = sp.Matrix([sp.diff(f_x, var) for var in x])

# Display the result
print("f(x) = ", f_x)
print("Gradient of f(x) = ", gradient_f_x)

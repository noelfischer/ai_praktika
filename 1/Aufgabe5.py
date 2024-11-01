# Import sympy for symbolic differentiation
import sympy as sp

# Define the variables
x, y = sp.symbols('x y')

# a)
F_a = sp.Matrix([x**2 + y**2, y**3])

# Compute the Jacobian of F_a with respect to [x, y]
Jacobian_a = F_a.jacobian([x, y])

print("Jacobian of F_a: ", Jacobian_a)




# b)
F_b = sp.Matrix([x**2 + y**2, x*y + 2*sp.cos(x)])

# Compute the Jacobian of F_b with respect to [x, y]
Jacobian_b = F_b.jacobian([x, y])

print("Jacobian of F_b: ", Jacobian_b)
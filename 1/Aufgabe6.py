# Importing sympy for symbolic differentiation
import sympy as sp

# Define variables
x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2')

# Step a: Define the function f(y1, y2)
f_y = y1**2 + 2*y2
g_x = x1*x2


# Start by calculating the derivative df/dy of f . This will be a single row-vector with 2 entries.
df_dy = sp.Matrix([sp.diff(f_y, y1), sp.diff(f_y, y2)])

# Next, we define the helper function
H_x = sp.Matrix([[g_x], [x1]])

# Now find the derivative dH/dx of this function. 
dH_dx = H_x.jacobian([x1, x2])

# Step c: Substitute y1 = x1 * x2 and y2 = x1 in df/dy
df_dy_sub = df_dy.subs({y1: x1 * x2, y2: x1})


# Step d: Now applying the chain rule correctly
dF_dx = df_dy_sub.T * dH_dx

print("df/dy: ", df_dy)
print("dF/dx: ", df_dy_sub)
print("dH/dx: ", dH_dx)
print("dF/dx: ", dF_dx)

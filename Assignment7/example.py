from sympy import symbols, solve, Symbol, diff, dsolve, sqrt
from sympy.physics.vector import dynamicsymbols

# Define Constants
t = Symbol("t")
tf = Symbol("t_f")
nu = Symbol("nu")
k = Symbol("k")
u = Symbol("u")
xf = Symbol("x_f")
lamb = Symbol("lambda")
c = Symbol("c")

x = dynamicsymbols("x")
xdot = x.diff()

x0 = 0
t0 = 0

phi = tf
L = k * u ** 2
psi = xf - 1

#u = (-lamb / (2 * k))
# Define G and Hamiltonian
G = phi + nu * (xf - 1)
H = L + lamb * u

lambdot = -diff(H, x)
zero = diff(H, u)

# Solve Equations
lamb = c

Hf = -diff(G, tf)
lamb_f = diff(G, xf)


print()


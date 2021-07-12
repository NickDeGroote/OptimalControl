from sympy import symbols, diff, Symbol, factor, dsolve, pprint, solve, substitution, integrate, sqrt, simplify
from sympy.physics.mechanics import dynamicsymbols


x = dynamicsymbols("x")
lamb = symbols("lambda")
t = Symbol("t")
a = Symbol("a")
c = Symbol("c")
t0 = Symbol("t_0")
tf = Symbol("t_f")
xdot = x.diff("t")

u = Symbol("u")
H = (1 + u**2) ** (1/2) / t - lamb * u

lambdot = -diff(H, x)
lambdot.subs(lamb, c)
zero = diff(H, u)

lambdot_deriv = lamb.diff("t")
#lambdot_mz = lambdot - zero

#eq = xdot + a**2 * x * t - a**2 * x * tf
#lamb_int = dsolve(eq)

#test = integrate(x, t)

#eq2 = (1 / t) * (u / sqrt(1 + u**2)) + 1

#zero_subs = zero.subs(lamb, lamb_int)
u_solve = solve(zero, u)

#test = solve(zero, u)

#x_int = dsolve(xdot - test[1])

#pprint(test[0])
#pprint(x_int)

#eq3 = -1 * t * sqrt(-1 / (1**2 * t**2 - 1))

integral = integrate(eq4, t)
pprint(simplify(integral))
print(simplify(integral))
from sympy import symbols, hessian, latex, pretty
from Assignment2.A2_Utilities import solve_double_eq_constraint


x, y, z = symbols("x y z")
J = (1 / 2) * (x ** 2 + y ** 2 + z ** 2)
g1 = x + 2 * y - z - 3
g2 = x - y + 2 * z - 12

soln = solve_double_eq_constraint(cost_function=J, constraint1=g1, constraint2=g2)

hess = hessian(J, [x, y, z])
print("\nHessian:")
print(pretty(hess))
print(latex(hess))
print(hess.eigenvals())

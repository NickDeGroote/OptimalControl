from sympy import symbols, hessian, latex, pretty
from Assignment2.A2_Utilities import solve_single_eq_constraint


x1, x2 = symbols("x1 x2")
J = x1 + x2
g = x1 ** 2 + x1 * x2 + x2 ** 2 - 1

soln = solve_single_eq_constraint(cost_function=J, constraint=g)

hess = hessian(J, [x1, x2])
print("\nHessian:")
print(pretty(hess))
print(latex(hess))
print(hess.eigenvals())

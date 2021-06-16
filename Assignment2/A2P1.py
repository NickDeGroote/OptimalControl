from sympy import symbols, hessian, latex, pretty
from Assignment2.A2_Utilities import solve_single_eq_constraint


x, y = symbols("x y")
J = x ** 2 + y ** 2
g = x * y - 1

soln = solve_single_eq_constraint(cost_function=J, constraint=g)

hess = hessian(J, [x, y])
print("\nHessian:")
print(pretty(hess))
print(latex(hess))
print(hess.eigenvals())

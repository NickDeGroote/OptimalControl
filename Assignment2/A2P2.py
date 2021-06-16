from sympy import symbols, exp, hessian, pretty, latex
from Assignment2.A2_Utilities import solve_single_eq_constraint


x, y = symbols("x y")
J = exp(x) * (4 * x ** 2 + 2 * y ** 2 + 4 * x * y + 2 * y + 1)
g = 0

soln = solve_single_eq_constraint(cost_function=J, constraint=g)

hess = hessian(J, [x, y])

# x = -3/2
# y = 1
print("\nHessian:")
hess_eval = hess.subs([(x, -3 / 2), (y, 1 / 2)])
print(pretty(hess_eval))
print(latex(hess))
print(latex(hess_eval))
print(hess_eval.eigenvals())

hess_eval = hess.subs([(x, 1 / 2), (y, -1)])
print(pretty(hess_eval))
print(latex(hess))
print(latex(hess_eval))
print(hess_eval.eigenvals())

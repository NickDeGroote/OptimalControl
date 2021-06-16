from sympy import symbols, exp, hessian, pretty, latex, simplify
from Assignment2.A2_Utilities import solve_ellipse_eq_constraint


x, y, a, b = symbols("x y a b")
J = 2 * 2 * x + 2 * 2 * y
g = (x ** 2 / a ** 2) + (y ** 2 / b ** 2) - 1

soln = solve_ellipse_eq_constraint(cost_function=J, constraint=g)
print(latex(simplify(4 * (soln[1][1] + soln[1][2]))))
hess = hessian(J, [x, y])

# x = -3/2
# y = 1
"""
print("\nHessian:")
hess_eval = hess.subs([(x, -3/2), (y, 1/2)])
print(pretty(hess_eval))
print(latex(hess))
print(latex(hess_eval))
print(hess_eval.eigenvals())

hess_eval = hess.subs([(x, 1/2), (y, -1)])
print(pretty(hess_eval))
print(latex(hess))
print(latex(hess_eval))
print(hess_eval.eigenvals())
"""

from sympy import symbols, hessian, latex, pretty
from Assignment2.A2_Utilities import solve_single_ineq_constraint


x, y, z = symbols("x y z")
J = x ** 2 + y ** 2
g = x * y - 1

soln = solve_single_ineq_constraint(cost_function=J, constraint=g)
hess = hessian(J, [x, y])

print("\nHessian:")
hess_eval = hess.subs([(x, -1), (y, -1)])
print(pretty(hess_eval))
print(latex(hess))
print(latex(hess_eval))
print(hess_eval.eigenvals())

hess_eval = hess.subs([(x, 1), (y, 1)])
print(pretty(hess_eval))
print(latex(hess))
print(latex(hess_eval))
print(hess_eval.eigenvals())

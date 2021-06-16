from sympy import symbols, hessian, latex, pretty, pi, numbered_symbols
from Assignment2.A2_Utilities import solve_single_eq_cylinder


r, h, c = symbols("r h c")
J = pi * r ** 2 * h
g = 2 * pi * r * h + 2 * pi * r ** 2 - c

soln = solve_single_eq_cylinder(cost_function=J, constraint=g)
list(soln)

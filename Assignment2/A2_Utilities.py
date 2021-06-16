from sympy import symbols, pretty, Matrix, solve, latex
from sympy.utilities.iterables import ordered


def solve_single_eq_constraint(
    cost_function: symbols, constraint: symbols, printing: bool = True
) -> symbols:
    gradient = lambda f, v: Matrix([f]).jacobian(v)
    lamb = symbols("lambda")
    lagrangian = cost_function - lamb * constraint
    vars = list(ordered(lagrangian.free_symbols))
    grad = gradient(lagrangian, vars)
    solution = solve(grad)
    if printing:
        print_steps(cost_function, constraint, lagrangian, grad, solution)
    return solution


def solve_double_eq_constraint(
    cost_function: symbols,
    constraint1: symbols,
    constraint2: symbols,
    printing: bool = True,
) -> symbols:
    gradient = lambda f, v: Matrix([f]).jacobian(v)
    nu1, nu2 = symbols("nu1 nu2")
    lagrangian = cost_function + nu1 * constraint1 + nu2 * constraint2
    vars = list(ordered(lagrangian.free_symbols))
    grad = gradient(lagrangian, vars)
    solution = solve(grad)
    if printing:
        print_steps(cost_function, constraint1, lagrangian, grad, solution)
    return solution


def solve_single_eq_cylinder(
    cost_function: symbols, constraint: symbols, printing: bool = True
) -> symbols:
    gradient = lambda f, v: Matrix([f]).jacobian(v)
    lamb = symbols("lambda")
    lagrangian = cost_function - lamb * constraint
    vars = list(ordered(lagrangian.free_symbols))[1:]
    grad = gradient(lagrangian, vars)
    solution = solve(grad)
    if printing:
        print_steps(cost_function, constraint, lagrangian, grad, solution)
    return solution


def solve_ellipse_eq_constraint(
    cost_function: symbols, constraint: symbols, printing: bool = True
) -> symbols:
    gradient = lambda f, v: Matrix([f]).jacobian(v)
    lamb, x, y = symbols("lambda x y")
    lagrangian = cost_function - lamb * constraint
    vars = list(ordered(lagrangian.free_symbols))[2:3]
    grad = gradient(lagrangian, vars)
    solution = solve(grad, vars)
    if printing:
        print_steps(cost_function, constraint, lagrangian, grad, solution)
    return solution


def solve_single_ineq_constraint(
    cost_function: symbols, constraint: symbols, printing: bool = True
) -> symbols:
    gradient = lambda f, v: Matrix([f]).jacobian(v)
    lamb, alpha = symbols("lambda alpha")
    lagrangian = cost_function + lamb * (constraint + alpha ** 2)
    vars = list(ordered(lagrangian.free_symbols))
    grad = gradient(lagrangian, vars)
    solution = solve(grad)
    if printing:
        print_steps(cost_function, constraint, lagrangian, grad, solution)
    return solution


def print_steps(cost_function, constraint, lagrangian, gradient, solution):
    print("Cost Function:")
    print(pretty(cost_function))
    print(latex(cost_function))

    print("\nConstraint:")
    print(pretty(constraint))
    print(latex(constraint))

    print("\nLagrangian:")
    print(pretty(lagrangian))
    print(latex(lagrangian))

    print("\nGradient:")
    print(pretty(gradient))
    print(latex(gradient.transpose()))
    print(latex(Matrix([0, 0, 0])))

    print("\nSolution:")
    print(pretty(solution))
    print(latex(solution))

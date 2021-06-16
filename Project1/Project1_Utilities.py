from sympy import symbols, pretty, Matrix, solve, latex, zeros
from sympy.utilities.iterables import ordered
from typing import List, Tuple


def solve_multi_ineq_constraint(
    cost_function: symbols, constraints: List[symbols], printing: bool = True
) -> List[Tuple]:
    """
    :param cost_function: The multi-variable function to be optimized
    :param constraints: The multi-variable constraints on the cost function
    :param printing: Whether or not the augmented cost function and gradient will be printed
    :return: All potential solutions to the problem
    """
    num_constraints = len(constraints)
    lambdas = symbols("lambda0:%d" % num_constraints)  # create N lambda variables
    alphas = symbols("alpha0:%d" % num_constraints)  # create N alpha variables
    gradient = lambda f, v: Matrix([f]).jacobian(v)  # Lambda function to find gradient
    acf = cost_function  # Initialize augmented cost function to original cost function
    for i in range(
        num_constraints
    ):  # Add to augmented cost function for num constraints
        acf += lambdas[i] * (constraints[i] + alphas[i] ** 2)
    vars = list(ordered(acf.free_symbols))  # Get a list of all independent variables
    grad = gradient(acf, vars)  # Find the gradient of the augmented cost function
    solution = solve(grad, vars)  # Solve the system of equations
    if printing:  # Print the augmented cost function and Jacobian
        print_steps(acf, grad, len(vars))
    return solution


def get_best_solution(cost_function: symbols, solutions: List[Tuple]):
    """
    :param cost_function: The multi-variable function to be optimized
    :param solutions: A list of all potential solutions
    :return: The best cost and best found solution
    """
    best_cost = float("inf")  # Initialize best cost to infinity
    x, y, z = symbols("x y z")  # Define design variables
    best_solution = None  # Initialize best solution to None
    for solution in solutions:  # Loop through all possible solutions
        real_flag = not any(
            element.is_imaginary for element in solution
        )  # Test if all elements are real
        cost = cost_function.evalf(  # Substitute into cost function
            subs={x: solution[-3], y: solution[-2], z: solution[-1]}
        )
        if (
            cost < best_cost and real_flag
        ):  # Update if a better cost is found and a valid solution
            best_cost = cost
            best_solution = solution
    return best_cost, best_solution


def print_steps(lagrangian: symbols, gradient: symbols, num_vars: int):
    """
    :param lagrangian: The augmented cost function
    :param gradient: The Jacobian of the augmented cost function
    :param num_vars: Number of equations in the system
    :return: None
    """
    print("\nLagrangian:")
    print(pretty(lagrangian))
    print(latex(lagrangian))

    print("\nGradient:")
    print(pretty(gradient))
    print(latex(gradient.transpose()))
    print(latex(zeros(1, num_vars)))

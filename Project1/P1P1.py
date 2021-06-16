import time

from sympy import symbols
from Project1.Project1_Utilities import solve_multi_ineq_constraint, get_best_solution


x, y, z = symbols("x y z")  # Define design variables
J = -5 * x - 4 * y - 6 * z  # Define cost function

# Define all 6 constraints
theta1 = x - y + z - 20
theta2 = 3 * x + 2 * y + 4 * z - 42
theta3 = 3 * x + 2 * y - 30
theta4 = -x
theta5 = -y
theta6 = -z

# Put constraints into a list
constraints = [theta1, theta2, theta3, theta4, theta5, theta6]

start_time = time.time()
# Call function for solving a constrained optimization problem with multiple constraints
soln = solve_multi_ineq_constraint(cost_function=J, constraints=constraints)
best_cost, best_solution = get_best_solution(J, soln)  # Find the best solution from all possible
print("--- %s seconds ---" % (time.time() - start_time))
print(best_solution)
print(best_cost)

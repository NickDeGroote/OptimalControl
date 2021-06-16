import time
import numpy as np


def dp_solve(domain_x, domain_u, a, b, delta_t, lamb, N, step=0.02, use_dp=True):
    j12_star = {}
    points_list = []
    for x in np.arange(domain_x[0], domain_x[1] + 0.1, step):
        best_cost = float("inf")
        best_x = None
        for u in np.arange(domain_u[0], domain_u[1] + 0.1, step):
            next_state = x + u
            if use_dp:
                if next_state not in j12_star.keys():
                    j12_star[next_state] = get_last_optimum(next_state, domain_u, step)
            else:
                j12_star[next_state] = get_last_optimum(next_state, domain_u, step)
            cost = 2 * u ** 2 + j12_star[next_state]
            if cost < best_cost:
                best_cost = cost
                best_x = x
        points_list.append((best_x, best_cost))
        # print("Best Point: {:.2f}, Best Cost: {:.3f}".format(best_x, best_cost))
    return points_list


def get_last_optimum(x, domain_u, step):
    best_cost = float("inf")
    best_x = None
    for u in np.arange(domain_u[0], domain_u[1] + 0.1, step):
        next_state = x + u
        cost = next_state ** 2 + 2 * u ** 2
        if cost <= best_cost:
            best_cost = cost
            best_x = x
    return best_cost

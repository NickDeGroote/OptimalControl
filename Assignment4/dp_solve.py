import time
import numpy as np


def dp_solve(domain_x, domain_u, a, b, delta_t, lamb=2, N=2, step=0.5, use_dp=True):
    j_star = {}
    u_star = {}
    for x in np.arange(domain_x[0], domain_x[1] + 0.1, step):
        if use_dp:
            val = get_last_optimum(x, domain_x, domain_u, a, step, lamb, j_star, u_star, N)
        else:
            val = get_last_optimum(x, domain_x, domain_u, a, step, lamb, j_star, u_star, N)
        print(val)
    return j_star, u_star


def get_last_optimum(x, domain_x, domain_u, a, step, lamb, j_star, u_star, N, use_dp=True):
    best_cost = float("inf")
    best_u = None
    # key = "x(" + str(N) + ") = " + str(x) + ", J*[" + str(N-1) + ":end]" + "(" + str(x) + ")"
    key = (N - 1, round(x, 4))
    if use_dp and key in j_star.keys():
        return j_star[key]

    for u in np.arange(domain_u[0], domain_u[1] + 0.1, step):
        next_state = (1 + a) * x + u
        if N == 1:
            new_cost = next_state ** 2 + lamb * u ** 2
        else:
            new_cost = lamb * u ** 2 + get_last_optimum(
                next_state,
                domain_x,
                domain_u,
                a,
                step,
                lamb,
                j_star,
                u_star,
                N - 1,
                use_dp,
            )
        if new_cost <= best_cost:
            best_cost = new_cost
            best_u = u

    j_star[key] = best_cost
    u_star[key] = best_u

    return j_star[key]

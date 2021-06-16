import time
from Assignment4.dp_solve import dp_solve


start_time = time.time()
opt_vals = dp_solve(
    domain_x=[0, 1.5],
    domain_u=[-1, 1],
    a=0,
    b=1,
    delta_t=0.5,
    lamb=2,
    N=2,
    step=0.02,
    use_dp=True,
)
end_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
print(opt_vals[0])

i = 0
for (key1, value1), (key2, value2) in zip(opt_vals[0].items(), opt_vals[1].items()):
    if key1[0] == 0 and (0 <= key1[1] <= 1.5):
        print(
            "J^*_{{ {}{} }}({:.2f}) = {:.4f} \\;\\;\\;\\;\\;\\;\\;\\; u^*(k)_{{ {}{} }}({:.2f}) = {:.4f} \\\\".format(
                key1[0], 2, key1[1], value1, key2[0], 2, key2[1], value2
            )
        )

for (key1, value1), (key2, value2) in zip(opt_vals[0].items(), opt_vals[1].items()):
    if key1[0] == 1 and (0 <= key1[1] <= 1.5):
        print(
            "J^*_{{ {}{} }}({:.2f}) = {:.4f} \\;\\;\\;\\;\\;\\;\\;\\; u^*(k)_{{ {}{} }}({:.2f}) = {:.4f} \\\\".format(
                key1[0], 2, key1[1], value1, key2[0], 2, key2[1], value2
            )
        )

print(opt_vals[1])

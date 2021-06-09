fixed_cost, variable_cost, selling_cost = map(int, input().split())

if variable_cost < selling_cost:
    count = - fixed_cost / (variable_cost - selling_cost)
    print(int(count) + 1)
else:
    print(-1)

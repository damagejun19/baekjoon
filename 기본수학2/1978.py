num_case = int(input())
num_list = list(map(int, input().split()))
count = 0

for i in num_list:
    num_factors = 0

    if i == 1:
        count -= 1

    for j in range(2, i):
        if i % j == 0:
            num_factors += 1
            break

    if num_factors == 0:
        count += 1

print(count)





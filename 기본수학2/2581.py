first_num = int(input())
second_num = int(input())
num_list = [i for i in range(first_num, second_num + 1)]
prime_num_list = []

for i in num_list:
    num_count = 0

    if i == 1:
        continue

    for j in range(2, i):
        if i % j == 0:
            num_count += 1
            break
    if num_count == 0:
        prime_num_list.append(i)

if len(prime_num_list) == 0:
    print(-1)
else:
    print(sum(prime_num_list))
    print(prime_num_list[0])






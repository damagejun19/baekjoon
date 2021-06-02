count = 0
n = int(input())
int_n = n

while True:
    first = n // 10 + n % 10
    second = (n % 10) * 10 + first % 10

    n = second
    count += 1

    if int_n == second:
        break

print(count)
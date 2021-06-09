import math

T = int(input())

for i in range(T):
    X, Y = map(int, input().split())
    dis = Y - X

    if dis <= 3:
        print(dis)
    else:
        n = int(math.sqrt(dis))
        if dis == n**2:
            print(2 * n - 1)
        elif n**2 < dis <= n**2 + n:
            print(2 * n)
        else:
            print(2 * n + 1)







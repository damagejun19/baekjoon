# 1712

# A, B, C = map(int, input().split())
#
# if B >= C:
#     print(-1)
# else:
#     net_profit = int(A / (C - B)) + 1
#     print(net_profit)

# 2292

# test_case = int(input())
# count = 0
#
# while True:
#     count += 1
#     end_point = 3 * count**2 - 3 * count + 1
#
#     if test_case <= end_point:
#         print(count)
#         break

# 1193
# num = int(input())
# n = 0
#
# while True:
#     n += 1
#     floor = (n * (n + 1)) / 2
#     if num <= floor:
#         break
#
# if n % 2 != 0:
#     x = floor - num + 1
#     top = x
#     bottom = (n + 1) - x
# else:
#     x = floor - num + 1
#     top = (n + 1) - x
#     bottom = x
#
# print('%d/%d' % (top, bottom))

# 2869
# import math
# X, Y, Z = map(int, input().split())
# print(math.ceil((Z - Y) / (X - Y)))

# 10250
# test_case = int(input())
#
# for i in range(test_case):
#     H, W, N = map(int, input().split())
#
#     floor = N % H
#     room_num = N // H + 1
#
#     if floor == 0:
#         floor = H
#         room = N // H
#
#     print(floor * 100 + room_num)

# 2775
# test = int(input())
#
# for i in range(test):
#     floor = int(input())
#     room_num = int(input())
#     floor_zero = [i for i in range(1, room_num + 1)]
#
#     for j in range(floor):
#         for k in range(1, room_num):
#             floor_zero[k] = floor_zero[k - 1] + floor_zero[k]
#     print(floor_zero[-1])

# 2839

# n_kg = int(input())
# count = 0
#
# while True:
#     if n_kg % 5 == 0:
#         print(n_kg // 5 + count)
#         break
#     n_kg -= 3
#     count += 1
#
#     if n_kg < 0:
#         print(-1)
#         break

# 1011
import math
T = int(input())

for i in range(T):
    X, Y = map(int, input().split())
    dis = Y - X
    n = int(math.sqrt(dis))

    if dis <= 3:
        print(dis)
    elif n ** 2 == dis:
        print(2*n - 1)
    elif n ** 2 < dis <= n ** 2 + n:
        print(2 * n)
    else:
        print(2*n + 1)
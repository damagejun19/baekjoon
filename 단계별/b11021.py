T = int(input())

for i in range(T):
    first, second = map(int, input().split())

    print("Case #%d: %d" % (i + 1, first + second))
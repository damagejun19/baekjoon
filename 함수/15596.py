def solve(a):
    n = len(a)
    ans = 0

    for i in range(n):
        ans += a[i]
    return ans


a = [1, 2, 3]
print(solve(a))
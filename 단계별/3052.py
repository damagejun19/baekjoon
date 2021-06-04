num = [int(input()) for i in range(10)]
divide_num = [x % 42 for x in num]
diff_num = []

for i in divide_num:
    if i not in diff_num:
        diff_num.append(i)
print(len(diff_num))
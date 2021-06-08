first_num, second_num = map(str, input().split())
first_num = int(''.join(reversed(first_num)))
second_num = int(''.join(reversed(second_num)))

if first_num > second_num:
    print(first_num)
else:
    print(second_num)


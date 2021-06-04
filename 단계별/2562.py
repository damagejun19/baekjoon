num_list = []
idx = 0


for i in range(9):
    num = int(input())
    num_list.append(num)

max = num_list[0]

for i in range(9):
    if num_list[i] > max:
        max = num_list[i]
        idx = i
print(max)
print(idx + 1)



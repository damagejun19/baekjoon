num_list = [int(input()) for i in range(3)]
multi_list = str(num_list[0]*num_list[1]*num_list[2])
val = list(map(int, multi_list))

for i in range(10):
    print(val.count(i))
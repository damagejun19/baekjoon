num_of_sugar = int(input())
count = 0

while True:
    if num_of_sugar % 5 == 0:
        count += num_of_sugar // 5
        print(count)
        break
    elif num_of_sugar < 0:
        print(-1)
        break
    elif num_of_sugar % 5 != 0:
        num_of_sugar -= 3
        count += 1
def find_self_num():
    natural_num = set(range(1, 10001))
    generated_num = set()

    for i in range(1, 10001):
        for j in str(i):
            i = i + int(j)
        generated_num.add(i)

    self_num = sorted(natural_num - generated_num)

    for j in self_num:
        print(j)


find_self_num()

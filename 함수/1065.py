def han_soo():
    test_num = int(input())
    count = 99

    if test_num < 100:
        return test_num
    else:
        for i in range(100, test_num + 1):
            if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
                count += 1
    return count
print(han_soo())
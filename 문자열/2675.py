num_of_test_case = int(input())

for i in range(num_of_test_case):
    test_case = input().split()
    num_of_repetitions = int(test_case[0])
    alphanumeric = test_case[1]
    result = ""

    for j in range(len(alphanumeric)):
        result = result + alphanumeric[j]*num_of_repetitions
    print(result)
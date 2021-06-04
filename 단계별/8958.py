test_case_count = int(input())


for i in range(test_case_count):
    test_case = input()
    score1 = 1
    score = 0
    for j in range(len(test_case)):
        if test_case[j] == 'O':
            score = score + score1
            score1 += 1
        else:
            score1 = 1
    print(score)
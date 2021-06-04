test_case = int(input())

for i in range(test_case):
    num_of_student_and_score = list(map(int, input().split()))
    num_of_student = num_of_student_and_score[0]
    average = num_of_student_and_score[1:]

    over_average = [x for x in average if x > sum(average)/num_of_student]
    print('%.3f%%' % (len(over_average)/len(average) * 100))
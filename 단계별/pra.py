class_list = int(input())

for i in range(class_list):
    test_case = list(map(int, input().split()))
    num_of_students = test_case[0]
    average_of_students = test_case[1:]
    class_average = sum(average_of_students) / num_of_students
    over_average = 0

    for j in range(num_of_students):
        if average_of_students[j] > class_average:
            over_average += 1
    print('%.3f%%' % (over_average / num_of_students * 100))
test_case = int(input())

for i in range(test_case):
    floor = int(input())
    room_num = int(input())
    people = [i for i in range(1, room_num+1)]

    for j in range(floor):
        for k in range(1, room_num):
            people[k] = people[k] + people[k-1]
    print(people[-1])
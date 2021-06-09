test_num = int(input())
room = 1
while True:
    if test_num <= 1 + 3*(room - 1) * room:
        print(room)
        break
    room += 1

str = input()
alphabet_list = [chr(i) for i in range(ord('a'), ord('z')+1)]

for i in alphabet_list:
    print(str.find(i), end=" ")
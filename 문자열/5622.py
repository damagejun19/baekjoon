alpha_dict = {'ABC':3, 'DEF':4, "GHI":5, "JKL":6,
              "MNO":7, "PQRS":8, "TUV":9, "WXYZ":10}
dial = input()
count = 0

for i in dial:
    for j, k in alpha_dict.items():
        if i in j:
            count += k
print(count)
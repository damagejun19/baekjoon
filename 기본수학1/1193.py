X = int(input())
floor = 1
end = 1

while True:
    if X <= end:
        break
    floor += 1
    end += floor

if floor % 2 == 0:
    top = floor - (end - X)
    bottom = end - X + 1
else:
    top = end - X + 1
    bottom = floor - (end - X)

print('%d/%d' % (top, bottom))



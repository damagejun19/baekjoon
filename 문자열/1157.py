word = input().upper()
spelling = list(set(word))
count_spell = []

for i in spelling:
    count = word.count(i)
    count_spell.append(count)
print(count_spell.count(max(count_spell)))
if count_spell.count(max(count_spell)) > 1:
    print('?')
else:
    print(spelling[count_spell.index((max(count_spell)))])
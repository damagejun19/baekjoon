croatia_list = ['c=', 'c-', 'dz=', 'd-',
                'lj', 'nj', 's=', 'z=']
croatia_spell = input()

for i in croatia_list:
    croatia_spell = croatia_spell.replace(i, 'a')

print(len(croatia_spell))


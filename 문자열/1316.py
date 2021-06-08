num_of_words = int(input())
result = 0

for i in range(num_of_words):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1

print(result)
# word = 'aaaa'
# for i in range(len(word)-1):
#     print(word.find(word[i]), word.find(word[i+1]))
n = int(input())
score = list(map(int, input().split()))
new_score = [i/max(score) * 100 for i in score]

average = sum(new_score) / len(new_score)
print(average)
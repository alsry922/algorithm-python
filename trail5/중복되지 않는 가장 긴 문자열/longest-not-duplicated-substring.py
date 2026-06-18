from collections import defaultdict
word = list(input())
n = len(word)
word = [0] + word
# Please write your code here.
count = defaultdict(int)
j = 0
answer = 1
for i in range(1, n + 1):
    while j + 1 <= n and count[word[j + 1]] < 1:
        count[word[j + 1]] += 1
        j += 1
    answer = max(answer, j - i + 1)
    count[word[i]] -= 1
print(answer)
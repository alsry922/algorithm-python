from collections import defaultdict
word, k = input().split()
k = int(k)
n = len(word)
word = [0] + list(word)
# Please write your code here.
char = defaultdict(int)
distinct_num = 0
j = 0
answer = 0

for i in range(1, n + 1):
    while j + 1 <= n and distinct_num <= k:
        if distinct_num == k  and char[word[j + 1]] == 0:
            break
        char[word[j + 1]] += 1
        if char[word[j + 1]] == 1:
            distinct_num += 1
        j += 1

    answer = max(answer, j - i + 1)
    char[word[i]] -= 1
    if char[word[i]] == 0:
        distinct_num -= 1
    
print(answer)
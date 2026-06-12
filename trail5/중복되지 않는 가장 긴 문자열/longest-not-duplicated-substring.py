word = input()
n = len(word)
# Please write your code here.
substr = set()
substr.add(word[0])
j = 0
answer = 1
for i in range(n):
    while j + 1 < n and word[j + 1] not in substr:
        substr.add(word[j + 1])
        j += 1

    answer = max(answer, j - i + 1)
    substr.remove(word[i])

print(answer)
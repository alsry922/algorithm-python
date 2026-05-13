n = int(input())
word = input()

# Please write your code here.
pcnt = [0] * (n + 1) # 0 ~ i - 1 까지 c의 갯수
scnt = [0] * (n + 1) # i ~ n - 1까지 w의 갯수

for i in range(1, n + 1):
    if word[i - 1] == 'C':
        pcnt[i] = pcnt[i - 1] + 1
    else:
        pcnt[i] = pcnt[i - 1]

for i in range(n - 1, -1, -1):
    if word[i] == 'W':
        scnt[i] = scnt[i + 1] + 1
    else:
        scnt[i] = scnt[i + 1]

answer = 0
for i in range(n):
    if word[i] != 'O':
        continue
    
    answer += (pcnt[i] * scnt[i + 1])

print(answer)
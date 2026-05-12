n = int(input())
word = input()

# Please write your code here.
C = [0] * n
W = [0] * n

C[0] = 1 if word[0] == 'C' else 0
for i in range(1, n):
    cnt = 1 if word[i] == 'C' else 0
    C[i] = C[i - 1] + cnt

W[-1] = 1 if word[-1] == 'W' else 0
for i in range(n - 2, -1, -1):
    cnt = 1 if word[i] == 'W' else 0
    W[i] = W[i + 1] + cnt

answer = 0
for i in range(n):
    if word[i] == 'O' and 0 < i < n - 1:
        answer += (C[i - 1] * W[i + 1])
print(answer)
    
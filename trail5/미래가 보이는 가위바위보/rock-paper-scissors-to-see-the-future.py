N = int(input())
B = [input() for _ in range(N)]

# Please write your code here.
L = [0] * N
R = [0] * N

for char in 'HSP':
    cnt = 0
    for i in range(N):
        if B[i] == char:
            cnt += 1
        L[i] = max(L[i], cnt)

for char in 'HSP':
    cnt = 0
    for i in range(N - 1, -1, -1):
        if B[i] == char:
            cnt += 1
        R[i] = max(R[i], cnt)
answer = 0
for i in range(N - 1):
    answer = max(answer, L[i] + R[i + 1])

print(answer)
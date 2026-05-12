n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
L = [arr[0] for _ in range(n)]
R = [arr[-1] for _ in range(n)]

for i in range(1, n):
    L[i] = max(L[i - 1], arr[i])

for j in range(n - 2, -1, -1):
    R[j] = max(R[j + 1], arr[j])

answer = 0
for i in range(2, n - 2):
    answer = max(answer, arr[i] + L[i - 2] + R[i + 2])

print(answer)
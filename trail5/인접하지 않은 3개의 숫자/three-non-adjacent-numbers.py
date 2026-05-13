n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
pmax = [0] * (n) # 0 ~ i - 1 까지 최댓값
smax = [0] * (n) # i ~ n - 1 까지 최댓값

pmax[0] = arr[0]
for i in range(1, n):
    pmax[i] = max(pmax[i - 1], arr[i])

smax[-1] = arr[-1]
for i in range(n - 2, -1, -1):
    smax[i] = max(smax[i + 1], arr[i])

answer = 0
for i in range(n):
    if 2 <= i <= n - 3:
        answer = max(answer, arr[i] + pmax[i - 2] + smax[i + 2])

print(answer)
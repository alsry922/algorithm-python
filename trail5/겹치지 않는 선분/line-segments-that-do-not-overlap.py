n = int(input())
lines = sorted([tuple(map(int, input().split())) for _ in range(n)])

# Please write your code here.
MIN = -1000000
MAX = 1000000
pmax = [MIN] * (n + 1) # 0 ~ i-1 까지의 최대
smin = [MAX] * (n + 1) # i ~ n-1 까지의 최소

for i in range(1, n + 1):
    pmax[i] = max(pmax[i - 1], lines[i - 1][1])

for i in range(n - 1, -1, -1):
    smin[i] = min(smin[i + 1], lines[i][1])

cnt = 0
for i in range(n):
    x2 = lines[i][1]
    cnt += 1 if pmax[i] < x2 < smin[i + 1] else 0
print(cnt)
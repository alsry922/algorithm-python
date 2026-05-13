n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.
lines = sorted(lines, key=lambda x: x[0])
pmax = [-float('inf')] + [0] * n  # pmax[0]이 센티넬
smin = [0] * n + [float('inf')]   # smin[n]이 센티넬
for i in range(1, n + 1):
    pmax[i] = max(pmax[i - 1], lines[i - 1][1])  # 1부터 시작

for i in range(n - 1, -1, -1):
    smin[i] = min(smin[i + 1], lines[i][1])
    
answer = 0
for i in range(n):
    x1, x2 = lines[i]
    cross = not (pmax[i] < x2 and x2 < smin[i + 1])
    if not cross:
        answer += 1


print(answer)
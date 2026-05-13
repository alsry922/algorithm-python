n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.
lines = sorted(lines, key=lambda x: x[0])
pmax = [0] * n
smin = [0] * n
pmax[0] = lines[0][1]
for i in range(1, n):
    if lines[i][1] > pmax[i - 1]:
        pmax[i] = lines[i][1]
    else:
        pmax[i] = pmax[i - 1]
smin[-1] = lines[-1][1]
for i in range(n - 2, -1, -1):
    if lines[i][1] < smin[i + 1]:
        smin[i] = lines[i][1]
    else:
        smin[i] = smin[i + 1]
answer = 0
for i in range(n):
    cross = True
    x1, x2 = lines[i]
    if i == 0 and smin[i + 1] > x2: 
        cross = False
    elif i == n - 1 and pmax[i - 1] < x2:
        cross = False
    else:
        cross = not (pmax[i - 1] < x2 and smin[i + 1] > x2)
    if not cross:
        answer += 1

print(answer)
import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
L = [0 for _ in range(n)]
R = [0 for _ in range(n)]

for i in range(1, n):
    x1, y1 = x[i - 1], y[i - 1]
    x2, y2 = x[i], y[i]
    L[i] = L[i - 1] + abs(x1 - x2) + abs(y1 - y2)

for i in range(n - 2, -1, -1):
    x1, y1 = x[i], y[i]
    x2, y2 = x[i + 1], y[i + 1]
    R[i] = R[i + 1] + abs(x1 - x2) + abs(y1 - y2)

answer = sys.maxsize
for i in range(1, n - 1):
    x1, y1 = x[i - 1], y[i - 1]
    x2, y2 = x[i + 1], y[i + 1]
    answer = min(answer, L[i - 1] + R[i + 1] + abs(x1 - x2) + abs(y1 - y2))

print(answer)

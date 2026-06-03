n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# Please write your code here.
grid = [
    [0 for _ in range(1001)]
    for _ in range(1001)
]
a_candidates = [x - 1 for x, y in points]
b_candidates = [y - 1 for x, y in points]

answer = 1000

for px, py in points:
    grid[px][py] += 1

p = [
    [0 for _ in range(1001)]
    for _ in range(1001)
]

for i in range(1, 1001):
    for j in range(1, 1001):
        p[i][j] = p[i][j - 1] + p[i - 1][j] - p[i - 1][j - 1] + grid[i][j]

for a in a_candidates:
    for b in b_candidates:
        q1 = p[a][1000] - p[a][b]
        q2 = p[1000][1000] - p[1000][b] - p[a][1000] + p[a][b]
        q3 = p[1000][b] - p[a][b]
        q4 = p[a][b]
        answer = min(answer, max(q1, q2, q3, q4))

print(answer)
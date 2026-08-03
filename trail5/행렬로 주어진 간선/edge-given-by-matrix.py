import sys
input = sys.stdin.readline
n = int(input())
graph = [[0] * (n + 1)]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

for i in range(1, n + 1):
    graph[i][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(1, n + 1):
    print(*graph[i][1:])

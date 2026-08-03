import sys
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = sys.maxsize
# Please write your code here.
# dijkstra
# 특정 시작점으로부터 모든 지점까지의 최단거리를 구해주는 알고리즘
# O(V ^ 2), O((V + E) log V)
#   음수 가중치가 존재하면 안됨
# floyd warshall
# 모든 지점 쌍간의 최단거리를 구해주는 알고리즘
# 모든 지점에서 시작하여 dijkstra를 진행하는 것과 같은 결과
# O(V ^ 3)
#   음수 가중치가 존재해도 되지만, 음수 사이클이 존재해서는 안됨
dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0
for s, e, v in edges:
    dist[s][e] = min(dist[s][e], v)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            row.append(-1)
        else:
            row.append(dist[i][j])
    print(*row)
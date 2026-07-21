n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [
    [0 for _ in range(n + 1)] for _ in range(n + 1)
]
INF = float('inf')
visited = [False for _ in range(n + 1)]
# Please write your code here.
for start, end, value in edges:
    graph[start][end] = value
dist = [INF for _ in range(n + 1)]
dist[1] = 0
for i in range(1, n + 1):
    min_index = -1
    for j in range(1, n + 1):
        # 최단거리가 이미 구해진 거면 skip
        if visited[j]:
            continue
        if min_index == -1 or dist[min_index] > dist[j]:
            min_index = j
    #
    visited[min_index] = True
    for j in range(1, n + 1):
        # 간선이 존재하지 않으면 skip
        if graph[min_index][j] == 0:
            continue
        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

for i in range(2, n + 1):
    print(-1 if INF == dist[i] else dist[i])
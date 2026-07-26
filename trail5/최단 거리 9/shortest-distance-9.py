import sys, heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
INF = sys.maxsize
# Please write your code here.
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for s, e, v in edges:
    graph[s][e] = v
    graph[e][s] = v
dist = [INF for _ in range(n + 1)]
dist[start] = 0
visited = [False for _ in range(n + 1)]
path = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    min_index = -1
    for j in range(1, n + 1):
        if visited[j]:
            continue
        if min_index == -1 or dist[j] < dist[min_index]:
            min_index = j
    
    visited[min_index] = True
    for j in range(1, n + 1):
        if dist[min_index] + graph[min_index][j] < dist[j]:
            dist[j] = dist[min_index] + graph[min_index][j]
            path[j] = min_index

print(dist[end])
cur = end
vertices = [end]
while cur != start:
    cur = path[cur]
    vertices.append(cur)

print(*reversed(vertices))
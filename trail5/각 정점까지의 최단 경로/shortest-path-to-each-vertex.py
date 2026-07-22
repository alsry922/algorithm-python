import heapq
n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
INF = float('inf')
# Please write your code here.
for start, end, value in edges:
    graph[start].append((end, value))
    graph[end].append((start, value))

dist = [INF for _ in range(n + 1)]
dist[k] = 0
q = []
for i in range(1, n + 1):
    heapq.heappush(q, (dist[i], i))

while q:
    min_dist, cur_v = heapq.heappop(q)
    if min_dist > dist[cur_v]:
        continue
    for end, value in graph[cur_v]:
        if min_dist + value < dist[end]:
            dist[end] = min_dist + value
            heapq.heappush(q, (dist[end], end))
for i in range(1, n + 1):
    print(-1 if dist[i] == INF else dist[i])
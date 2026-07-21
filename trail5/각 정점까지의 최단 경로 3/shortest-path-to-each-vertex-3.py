import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)] # 인접리스트 그래프 구현
INF = float('inf')
dist = [INF for _ in range(n + 1)]
dist[1] = 0
# Please write your code here.
for start, end, value in edges:
    graph[start].append((end, value))

def dijkstra(graph):
    q = []

    for i in range(1, n + 1):
        heapq.heappush(q, (dist[i], i))
    
    while q:
        min_dist, cv = heapq.heappop(q)
        for end, value in graph[cv]:
            if min_dist + value < dist[end]:
                dist[end] = min_dist + value
                heapq.heappush(q, (dist[end], end))
dijkstra(graph)

for i in range(2, n + 1):
    print(-1 if INF == dist[i] else dist[i])

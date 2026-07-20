from collections import deque
import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
MAX = float('inF')
# Please write your code here.
dist = [MAX] * (n + 1)
graph = [
    [] for _ in range(n + 1)
]
for edge in edges:
    start, end, value = edge
    graph[start].append((end, value))


def dijkstra(graph, source):
    dist[source] = 0
    heap = []
    for v in range(1, n + 1):
        heapq.heappush(heap, (dist[v], v))

    while heap:
        cur_dist, u = heapq.heappop(heap)
        for end, value in graph[u]:
            alt = dist[u] + value
            if alt < dist[end]:
                dist[end] = alt
                heapq.heappush(heap, (alt, end))

dijkstra(graph, 1)
for i in range(2, n + 1):
    print(-1 if dist[i] == MAX else dist[i])

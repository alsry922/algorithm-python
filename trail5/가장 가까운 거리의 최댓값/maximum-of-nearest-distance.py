import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
a, b, c = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = sys.maxsize
graph = [[] for _ in range(n + 1)]
# Please write your code here.
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))

dist_abc = [INF for _ in range(n + 1)]

def dijkstra(start):
    dist = [INF for _ in range(n + 1)]
    dist[start] = 0
    heap = [(dist[start], start)]
    while heap:
        min_dist, cur_v = heapq.heappop(heap)
        if min_dist > dist[cur_v]:
            continue
        for e, v in graph[cur_v]:
            if min_dist + v < dist[e]:
                dist[e] = min_dist + v
                heapq.heappush(heap, (dist[e], e))

    
    for i in range(1, n + 1):
        dist_abc[i] = min(dist_abc[i], dist[i])
    
dijkstra(a)
dijkstra(b)
dijkstra(c)
answer = max(dist_abc[1:])
print(answer)
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
INF = sys.maxsize
graph = [[] for _ in range(n + 1)]
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))

for lst in graph:
    lst.sort()

def dijkstra(dist, heap):
    while heap:
        min_dist, cv = heapq.heappop(heap)
        if min_dist > dist[cv]:
            continue
        for e, v in graph[cv]:
            if min_dist + v < dist[e]:
                dist[e] = min_dist + v
                heapq.heappush(heap, (dist[e], e))

dist1 = [INF for _ in range(n + 1)]
dist1[start] = 0
q1 = [(dist1[start], start)]

dist2 = [INF for _ in range(n + 1)]
dist2[end] = 0
q2 = [(dist2[end], end)]
dijkstra(dist1, q1)
dijkstra(dist2, q2)
    
print(dist1[end])
path = [start]
cur = start
while cur != end:
    for i, v in graph[cur]:
        if dist1[cur] + v + dist2[i] == dist1[end]:
            cur = i
            path.append(cur)
            break

print(*path)
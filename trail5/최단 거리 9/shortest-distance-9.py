import sys, heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B = map(int, input().split())
INF = sys.maxsize
# Please write your code here.
graph = [[] for _ in range(n + 1)]
for start, end, value in edges:
    graph[start].append((end, value))
    graph[end].append((start, value))
dist = [INF for _ in range(n + 1)]
dist[A] = 0
path = [0 for _ in range(n + 1)]
heap = [(dist[A], A)]
while heap:
    min_dist, cur_v = heapq.heappop(heap)
    if min_dist > dist[cur_v]:
        continue
    
    for end, value in graph[cur_v]:
        if min_dist + value < dist[end]:
            dist[end] = min_dist + value
            path[end] = cur_v
            heapq.heappush(heap, (dist[end], end))
    
print(dist[B])
end = B
vertices = [end]
while end != A:
    end = path[end]
    vertices.append(end)
print(*reversed(vertices))
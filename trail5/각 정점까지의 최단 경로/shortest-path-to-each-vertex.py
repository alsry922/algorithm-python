import heapq
n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = float('inf')
graph = [[] for _ in range(n + 1)]
# Please write your code here.
for start, end, value in edges:
    graph[start].append((end, value))
    graph[end].append((start,value))
dist = [INF for _ in range(n + 1)]
dist[k] = 0
q = [(dist[i], i) for i in range(1, n + 1)]
heapq.heapify(q)

while q:
    # 최소 거리, 현재 노드(현재 노드까지 최소 거리)
    min_dist, cv = heapq.heappop(q)
    # 갱신되기 전 stale 요소는 skip함.
    if min_dist > dist[cv]:
        continue
    # cv와 연결된 노드들 탐색
    for end, value in graph[cv]:
        if min_dist + value < dist[end]:
            dist[end] = min_dist + value
            heapq.heappush(q, (dist[end], end))

for i in range(1, n + 1):
    print(-1 if dist[i] == INF else dist[i])
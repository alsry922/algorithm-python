import sys, heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
# 다익스트라 사용 조건
# 1. 모든 간선은 가중치를 가진다.
#   모든 가중치가 1이면 bfs로 더 간단하고 빠르게 해결 가능
# 2. 모든 가중치는 양수이다.
#   최단 거리를 heap에서 뽑을 때 이 노드의 최단거리가 확정되었다고 가정함(greedy)
#   음수 가중치가 존재하면, 이 전제가 깨지기 때문.
INF = sys.maxsize
graph = [[] for _ in range(n + 1)]
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))
for row in graph:
    row.sort()

dist = [INF for _ in range(n + 1)]
# 도착점을 시작점으로 해서 다익스트라 진행
dist[end] = 0
heap = [(dist[end], end)]

while heap:
    min_dist, cur_v = heapq.heappop(heap)
    if min_dist > dist[cur_v]:
        continue
    
    for e, v in graph[cur_v]:
        if min_dist + v < dist[e]:
            dist[e] = min_dist + v
            heapq.heappush(heap, (dist[e], e))
cur = start
path = [cur]
while cur != end:
    # cur 노드와 연결된 노드 v중 dist[v] + (cur과 v의 가중치) = dist[cur] 이 되는 v를 찾아야 함
    candidates = []
    for e, v in graph[cur]:
        if dist[cur] == dist[e] + v:
            cur = e
            break
    path.append(cur)
print(dist[start])
print(*path)


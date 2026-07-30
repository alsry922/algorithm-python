import sys, heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = sys.maxsize
# Please write your code here.
# dijkstra
# 특정 시점점부터 모든 정점까지의 최단 거리를 구해주는 알고리즘
# 모든 간선에 1 이상의 가중치가 존재해야 하며, 가중치에 음수는 없어야 한다.
#   - 모든 가중치가 1이면 bfs로 간단하고 더 빨리 문제를 해결할 수 있음.
#   - 음수 가중치가 존재하면, A -> B 보다 A -> C -> B 처럼 더 멀리 돌아오는 경로가
#     최단거리가 되는 경우가 존재할 수 있으므로, greedy 가정이 깨지기 때문.
#   - 사이클이 존재해도 괜찮음.
#   시간 복잡도는 O(V^2) or O(E log V)

# 지금 문제는 특정 도착점으로부터의 모든 정점의 최단 거리를 구해야 함.
# 이런 경우, 모든 간선을 뒤집어 도착점을 시작으로 dijkstra를 진행하면 됨.
# 지금 문제는 무방향 그래프이므로, 간선을 뒤집을 필요 없음
dist = [INF for _ in range(n + 1)]
dist[n] = 0
graph = [[] for _ in range(n + 1)]
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))
heap = [(dist[n], n)]
while heap:
    min_dist, cv = heapq.heappop(heap)
    if min_dist > dist[cv]:
        continue
    
    for e, v in graph[cv]:
        if min_dist + v < dist[e]:
            dist[e] = min_dist + v
            heapq.heappush(heap, (dist[e], e))

print(max(dist[1:]))
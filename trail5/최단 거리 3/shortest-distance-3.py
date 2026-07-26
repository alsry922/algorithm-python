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

# 각 노드별 최단 거리를 저장할 배열
dist = [INF for _ in range(n + 1)]
dist[start] = 0
# 각 노드별 최소 거리를 확정할 힙
heap = [(dist[start], start)]
while heap:
    min_dist, cur_v = heapq.heappop(heap)
    # 같은 노드가 여러 번 삽입될 수 있음.
    # 최소 거리를 가진 요소를 heap에서 뽑는 경우, 이 노드는 최소거리가 정해진 것이라고 가정하기 때문에(greedy)
    # 현재 cur_v의 확정된 최단 거리와, min_dist 값이 다르면 stale 요소임.
    # 따라서 stale 요소는 skip함
    if min_dist > dist[cur_v]:
        continue

    for e, v in graph[cur_v]:
        if min_dist + v < dist[e]:
            dist[e] = min_dist + v
            heapq.heappush(heap, (dist[e], e))

print(dist[end])
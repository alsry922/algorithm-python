# 1 ~ N 정점 존재, N번은 학교, 나머지는 학생 집
# 두 정점 사이의 간선은 최대 1개, 무방향 그래프
# 다익스트라는 특정 정점에서부터 모든 정점까지의 최단거리를 구해줌
# 모든 정점에서부터 특정 도착점까지의 최단거리는 어떻게 구할까?
# 모든 간선을 뒤집고, 도착점을 시작점으로 다익스트라를 진행하면 됨.
# 현재 문제는 무방향 그래프이므로 간선을 뒤집을 필요 없음.
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
INF = sys.maxsize
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))
# 시작점부터 각 노드까지의 최단거리를 기록할 배열
dist = [INF for _ in range(n + 1)]
start = n
dist[start] = 0
# 각 탐색마다 최단거리를 찾도록 heap 선언
heap = [(dist[start], start)]
while heap:
    # heap에서 뽑힌 최소값을 가지는 노드는 최단 거리가 확정임.
    min_dist, cur_v = heapq.heappop(heap)
    # 최단 거리가 현재 dist에 저장된 최단거리와 다르다면 stale 요소임.
    # 같은 노드가 여러 번 heap에 추가될 수 있기 때문
    if min_dist > dist[cur_v]:
        continue
    
    # 현재 노드와 연결된 노드들 탐색
    for e, v in graph[cur_v]:
        # 현재 노드까지의 최단 거리와
        # 현재 노드 ~ e 까지의 가중치를 더한 것이
        # 현재 e 노드의 최단거리로 기록된 값보다 작으면
        # e 노드까지의 최단거리를 갱신
        if min_dist + v < dist[e]:
            dist[e] = min_dist + v
            heapq.heappush(heap, (dist[e], e))

print(max(dist[1:n]))
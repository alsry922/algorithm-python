import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = float('inf')
dist = [INF for _ in range(n + 1)]
dist[n] = 0
graph = [[] for _ in range(n + 1)]
# Please write your code here.
# 모든 정점으로부터 특정 도착점까지의 최단거리
# 특정 시작점에서 모든 정점까지의 최단거리를 구하는 알고리즘이 다익스트라
# 모던 정점에서부터 도착점까지릐 최단거리를 구하는 방법?
# 각 정점마다 다익스트라 알고리즘으로 시뮬레이션 해도 되지만,
# 모든 간선을 뒤집고, 도착점을 시작점으로하여 다익스트라 알고리즘을 시뮬레이션 해도 된다.
# 단방향인 경우에 해당하며, 양방향인 경우에는 모든 간선을 뒤집을 필요가 없다.

# N의 범위가 크기 때문에 heap을 이용하여 다익스트라 알고리즘을 구현한다.
# 모든 간선을 뒤집어서 그래프를 인접리스트로 구현한다.
for start, end, value in edges:
    graph[end].append((start, value))
# 힙에 시작점 넣고 다익스트라 시작
q = [(dist[n], n)]
while q:
    # 힙에서 최단거리가 구해진 정점 찾아서 제거
    min_dist, cur_v = heapq.heappop(q)
    # 같은 정점이 여러 번 heap에 들어갈 수 있음.
    # 이미 최단거리가 구해졌던 정점은 skip 함
    if min_dist > dist[cur_v]:
        continue
    # cur_v 정점과 연결된 노드를 탐색
    for end, value in graph[cur_v]:
        # 현재 end 정점까지의 거리가, cur_v에서 이어진 거리보다 크다면
        # 최단 거리를 갱신
        if min_dist + value < dist[end]:
            dist[end] = min_dist + value
            # 구해진 최단 거리를 큐에 삽입
            heapq.heappush(q, (dist[end], end))

print(max(dist[1:]))
            
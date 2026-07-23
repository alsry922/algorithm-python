import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
INF = float('inf')
dist = [INF for _ in range(n + 1)]
# 시작점은 최단거리가 0
dist[n] = 0
# Please write your code here.
# N번 노드(학교) 에서 집까지 가는 최단거리를 구하고, 그 중 최댓값을 출력
# 거리 1마다 1초의 이동시간이 걸림
# 다익스트라 -> 특정 시작점에서 모든 정점까지의 최단 거리를 구함
# 단방향 그래프에서 특정 도착점으로부터 모든 정점까지의 거리를 구하려면 모든 간선을 뒤집어주어야 함.

# 뒤집어서 그래프 구현
# N이 크니까 인접리스트로 O(E log V) 다익스트라로 구현해야 함.
for start, end, value in edges:
    graph[end].append((start, value))

# 우선순위 큐 만들기
q = [(dist[i], i) for i in range(1, n + 1)]
heapq.heapify(q)

# 큐에 원소가 남아있을 때까지 반복
while q:
    # cur_v와 cur_v까지의 최단 거리
    min_dist, cur_v = heapq.heappop(q)
    # cur_v의 최소값이 갱신되기 전 stale 값은 무시함
    # 같은 노드가 여러 번 삽입될 수 있기 때문임.
    if min_dist > dist[cur_v]:
        continue
    # cur_v와 연결된 노드들 탐색
    for end, value in graph[cur_v]:
        # 계산한 최단거리가 현재 end까지의 최단거리보다 작다면 갱신
        if min_dist + value < dist[end]:
            dist[end] = min_dist + value
            # 노드 추가
            heapq.heappush(q, (dist[end], end))

print(max(dist[1:]))
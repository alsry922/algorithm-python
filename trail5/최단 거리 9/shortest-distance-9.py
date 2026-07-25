import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
INF = sys.maxsize
# 다익스트라 알고리즘
# 특정 시작점에서부터 모든 정점까지의 최단 거리를 구해주는 알고리즘
#   다익스트라 알고리즘을 사용하기 위해서
#   1. 가중치가 있는 그래프
#       모든 간선에 거리/비용 개념의 가중치가 있어야 함.
#       간선의 가중치가 모두 1이라면 BFS로 더 간단하고 빠르게 구현 가능함.
#   2. 모든 간선에서 가중치는 양수이어야 함 -> 음수가 존재하면 greedy 가정이 깨지기 때문
#       모든 가중치가 양수면, 시작점(A)에서 특정 정점(C)에 도달하는 경우(알파)는
#       알파보다 멀리서 돌아서 C에 도착하는 경우(베타)보다 항상 작거나 같을 수밖에 없음.
#       그래서 힙에서 혹은 그래프에서 가장 작은 값을 골랐을 때 이 정점은 최단거리가 정해졌다고 가정함.
#       하지만 음수 가중치가 존재했을 때, 이미 최단거리가 확정된 정점(C)가, 더 멀리서 돌아와서 C에 도착한 경우보다 클 수가 있음.
#       이 경우는 벨만 포드 알고리즘을 사용해야 함.

# N이 1000이므로 O(N^2)가 가능함
# 근데, 일단 인접리스트로 구현해서 다익스트라 구현해보자
graph = [[] for _ in range(n + 1)]
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))
# 각 정점까지의 최단 거리를 기록할 dist
dist = [INF for _ in range(n + 1)]
# 시작점은 최단거리가 0임
dist[start] = 0
# i 정점에 도착하기 전 노드를 기록하기 위한 배열
path = [0] * (n + 1)
# q에 최소 거리가 확정된 노드를 삽입
q = [(0, start)]
# 다익스트라 시작
# 힙이 빌 때까지 반복
while q:
    # 최단 거리가 확정된 노드를 힙에서 제거
    min_dist, cv = heapq.heappop(q)
    # 최단 거리 확정 이전의 오래된 노드라면 무시
    if min_dist > dist[cv]:
        continue
    # cv 정점과 연결된 노드를 탐색
    for e, v in graph[cv]:
        # e 정점에 기록한 최소 거리를 갱신 가능하다면 갱신 후 힙에 삽입
        # path에도 e에 도달하기 전 노드를 기록
        if min_dist + v < dist[e]:
            dist[e] = min_dist + v
            path[e] = cv
            heapq.heappush(q, (dist[e], e))

vertices = []
x = end
vertices.append(x)
# x 가 시작점에 도달할 때까지 path 추적
while x != start:
    x = path[x]
    vertices.append(x)
# 최소 거리 출력
print(dist[end])
# path를 추적한 경로를 뒤집어서 출력
for ele in reversed(vertices):
    print(ele, end=' ')
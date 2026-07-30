# dijkstra
# dijkstra는 특정 시작점에서 모든 정점까지의 최단 거리를 구함
#   ex) 1에서 출발하여 2, 3, 4, 5까지의 최단거리. 노드 2에서 출발하는 경우의 결과는 따로 안 구해줌
#   음수 간선 허용하지 않음.
# floyd warshall
# 모든 정점 쌍(i, j)에 대해 i에서 j로 가는 최단거리를 한 번에 다 구함
#   ex) 1 -> 2 | 1 -> 3 | 2 -> 1 | 2 -> 3, ... 모든 조합의 최단거리가 결과로 나옴
#   음수 간선이 허용됨. but, 음수 싸이클이 있어서는 안됨. 사이클을 돌 때마다 총 거리가 계속 줄어들기 때문.
#   답이 마이너스 무한대로 발산함.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
INF = sys.maxsize
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for s, e, v in edges:
    graph[s][e] = min(graph[s][e], v)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(-1, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

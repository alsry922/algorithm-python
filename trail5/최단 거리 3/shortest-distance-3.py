import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
INF = sys.maxsize
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for s, e, v in edges:
    graph[s][e] = min(graph[s][e], v)
    graph[e][s] = min(graph[e][s], v)
dist = [INF for _ in range(n + 1)]
dist[start] = 0
visited = [False for _ in range(n + 1)]

for i in range(1, n + 1):
    min_index = -1
    for j in range(1, n + 1):
        # 방문한 노드는 건너뜀
        if visited[j]:
            continue
        # 최소값을 가지는 노드를 뽑음.
        if min_index == - 1 or dist[j] < dist[min_index]:
            min_index = j
    # 노드를 뽑는다는 것은 최단 거리가 확정되었다는 것임
    # 방문 표시
    visited[min_index] = True
    for j in range(1, n + 1):
        dist[j] = min(dist[j], dist[min_index] + graph[min_index][j])

print(dist[end])
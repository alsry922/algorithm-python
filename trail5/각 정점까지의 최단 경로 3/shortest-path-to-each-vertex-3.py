n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
INF = float('inf')
visited = [False for _ in range(n + 1)]
# Please write your code here.

for start, end, value in edges:
    graph[start][end] = value

dist = [INF for _ in range(n + 1)]
dist[1] = 0
for i in range(1, n + 1):
    min_index = -1
    # dist를 순회하며 최소 거리가 구해진 노드 뽑기
    for j in range(1, n + 1):
        # 이미 방문한 노드면 건너뛰기
        if visited[j] == True:
            continue 
        if min_index == - 1 or dist[j] < dist[min_index]:
            min_index = j
    # 최소 거리가 구해진 노드 방문 표시
    visited[min_index] = True
    for j in range(1, n + 1):
        # 최소 거리가 구해진 노드와 연결되지 않은 노드는 건너뛰기
        if graph[min_index][j] == 0:
            continue
        # 최소 거리가 구해진 노드와 j까지의 거리를 더한 값과,
        # 현재 j 노드까지의 최소 거리를 비교했을 때,
        # 전자가 더 작은 경우 갱신한다.
        if dist[min_index] + graph[min_index][j] < dist[j]:
            dist[j] = dist[min_index] + graph[min_index][j]

for i in range(2, n + 1):
    print(-1 if dist[i] == INF else dist[i])


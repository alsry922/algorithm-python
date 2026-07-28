# 다익스트라 알고리즘
# 특정 시작점부터 도달가능한 모든 정점까지의 최단 거리를 구해준다.
# 특정 정점에서부터 A, B, C 정점까지의 최단거리를 구하고 그 중 최댓값을 구해야 한다.
# N이 최대 100000이기 때문에 이 방법은 안됨
# 그럼 A, B, C는 정해졌으니 A, B, C 각각에서 시작해서 다익스트라를 구한다.
# 다익스트라로 distA, distB, distC를 구하고, 
# distA, distB, distC에서 모두 도달 가능한 정점 중 최댓값을 구하면 될 것 같다.
import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
a, b, c = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
INF = sys.maxsize
for s, e, v in edges:
    graph[s].append((e, v))
    graph[e].append((s, v))

distA = [INF for _ in range(n + 1)]
distA[a] = 0
heapA = [(distA[a], a)]

distB = [INF for _ in range(n + 1)]
distB[b] = 0
heapB = [(distB[b], b)]

distC = [INF for _ in range(n + 1)]
distC[c] = 0
heapC = [(distC[c], c)]

def dijkstra(dist, heap):
    while heap:
        min_dist, cv = heapq.heappop(heap)
        if min_dist > dist[cv]:
            continue
        for e, v in graph[cv]:
            if min_dist + v < dist[e]:
                dist[e] = min_dist + v
                heapq.heappush(heap, (dist[e], e))
dijkstra(distA, heapA)
dijkstra(distB, heapB)
dijkstra(distC, heapC)

answer = 0
for i in range(1, n + 1):
    if distA[i] == INF or \
        distB[i] == INF or \
        distC[i] == INF:
        continue

    answer = max(answer, min(distA[i], distB[i], distC[i]))
print(answer)
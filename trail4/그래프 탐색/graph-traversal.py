n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [False] * (n + 1)
# Please write your code here.
graph = [[] for _ in range(n + 1)]

for start, end in edges:
    graph[start].append(end)
    graph[end].append(start)


def dfs(curr_v):
    global answer
    for next_v in graph[curr_v]:
        if not visited[next_v]:
            visited[next_v] = True
            dfs(next_v)
            answer += 1

answer = 0
visited[1] = True
dfs(1)
print(answer)
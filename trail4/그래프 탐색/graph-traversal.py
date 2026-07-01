n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [False] * (n + 1)
# Please write your code here.
graph = [[] for _ in range(n + 1)]

for start, end in edges:
    graph[start].append(end)
    graph[end].append(start)


def dfs(curr_v):
    count = 0
    for next_v in graph[curr_v]:
        if not visited[next_v]:
            visited[next_v] = True
            count += 1 + dfs(next_v)
    
    return count

visited[1] = True
answer = dfs(1)
print(answer)
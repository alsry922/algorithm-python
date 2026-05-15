n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
pmax = [0] * (n + 1) # 0 ~ i-1 까지의 최댓값
smax = [0] * (n + 1) # i ~ n 까지의 최댓값

for i in range(1, n + 1):
    pmax[i] = max(pmax[i - 1], arr[i - 1])

for j in range(n - 1, -1, -1):
    smax[j] = max(smax[j + 1], arr[j])

for query in queries:
    x1, x2 = query[0] - 1, query[1] - 1
    print(max(pmax[x1], smax[x2 + 1]))
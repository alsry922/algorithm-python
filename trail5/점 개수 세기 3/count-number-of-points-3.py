from sortedcontainers import SortedSet
n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
nums = SortedSet(points)
cnt = 1
mapper = {}
for num in nums:
    mapper[num] = cnt
    cnt += 1

prefix_sum = [0 for _ in range(n + 1)]
for point in points:
    idx = mapper[point]
    prefix_sum[idx] += 1

for i in range(1, n + 1):
    prefix_sum[i] += prefix_sum[i - 1]

for query in queries:
    x1, x2 = query
    lx, rx = mapper[x1], mapper[x2]
    print(prefix_sum[rx] - prefix_sum[lx - 1])
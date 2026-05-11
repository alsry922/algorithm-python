from sortedcontainers import SortedSet
import bisect
import sys
input = sys.stdin.readline
n, q = map(int, input().split())
points = sorted(list(map(int, input().split())))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
# mapper = {}
# cnt = 1
# for point in points:
#     mapper[point] = cnt
#     cnt += 1

# prefix_sum = [0 for _ in range(n + 1)]
# for point in points:
#     prefix_sum[mapper[point]] += 1

# for i in range(1, n + 1):
#     prefix_sum[i] = prefix_sum[i - 1] + 1

out = []
for query in queries:
    l, r = query
    li = bisect.bisect_left(points, l)
    ri = bisect.bisect_right(points, r)
    out.append(str(ri - li))
print('\n'.join(out))
from sortedcontainers import SortedSet

n, q = map(int, input().split()) # 점 개수, 질의 수
points = SortedSet(list(map(int, input().split())))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
map = {}
cnt = 1
for point in points:
    map[point] = cnt
    cnt += 1

comp_points = [0] + [1 for _ in range(len(points))]

prefix_sum = [0 for _ in range(len(points) + 1)]
for i in range(1, len(comp_points)):
    prefix_sum[i] = prefix_sum[i - 1] + comp_points[i]

out = []
for query in queries:
    # 질의의 나오는 좌표를 압축
    start, end = map[query[0]], map[query[1]]
    out.append(str(prefix_sum[end] - prefix_sum[start - 1]))

print('\n'.join(out))
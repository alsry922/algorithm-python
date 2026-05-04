n, q = map(int, input().split()) # 점 개수, 주어지는 범위 개수
points = list(map(int, input().split()))
ranges = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
MAX_N = 1000000
nums = [0 for _ in range(MAX_N + 1)]
for point in points:
    nums[point] = 1

prefix_sum = [0 for _ in range(MAX_N + 1)]

for i in range(1, MAX_N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]

for range in ranges:
    start, end = range
    print(prefix_sum[end] - prefix_sum[start] + nums[start])


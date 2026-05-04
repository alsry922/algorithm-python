N, K, B = map(int, input().split())
missing = set([int(input()) for _ in range(B)])

# Please write your code here.
nums = [i for i in range(1, N + 1)]
not_exists = [0] + [1 if ele in missing else 0 for ele in nums]
prefix_sum = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + not_exists[i]

answer = 100000
for i in range(1, N - K + 2):
    cnt = prefix_sum[i + K - 1] - prefix_sum[i - 1]
    answer = min(answer, cnt)
print(answer)
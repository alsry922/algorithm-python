n = int(input())
numbers = [0] + [int(input()) for _ in range(n)]

# Please write your code here.

MOD = 7
max_idx = [-1] * MOD # 특정 나머지가 등장한 인덱스 중 최대 인덱스
min_idx = [n + 1] * MOD # 특정 나머지가 등장한 인덱스 중 최소 인덱스
min_idx[0] = max_idx[0] = 0
sum_div7 = 0
for i in range(1, n + 1):
    sum_div7 += numbers[i]
    sum_div7 %= MOD
    
    max_idx[sum_div7] = max(max_idx[sum_div7], i)
    min_idx[sum_div7] = min(min_idx[sum_div7], i)

# print(numbers)
# print(remainders)
# print(min_idx)

answer = 0

for i in range(MOD):
    answer = max(answer, max_idx[i] - min_idx[i])

print(answer)
n = int(input())
numbers = [0] + [int(input()) for _ in range(n)]

# Please write your code here.

remainders = [0] * (n + 1)
min_idx = [-1] * 7
sum_val = 0
for i in range(1, n + 1):
    sum_val += numbers[i]
    remainders[i] = sum_val % 7

# print(numbers)
# print(remainders)
# print(min_idx)

answer = 0
for i in range(n + 1):
    if min_idx[remainders[i]] == -1:
        min_idx[remainders[i]] = i
    answer = max(answer, i - min_idx[remainders[i]]
    )

print(answer)
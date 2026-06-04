n = int(input())
numbers = [0] + [int(input()) for _ in range(n)]

# Please write your code here.
remainders = [0] * (n + 1)
counting = [0] * 7
sum_val = 0
for i in range(1, n + 1):
    sum_val += numbers[i]
    remainders[i] = sum_val % 7

j = 0
answer = 0

for i in range(1, n + 1):
    counting[remainders[i]] = max(counting[remainders[i]], i)

for i in range(n + 1):
    if counting[remainders[i]] != 0:
        answer = max(answer, counting[remainders[i]] - i)
    
print(answer)
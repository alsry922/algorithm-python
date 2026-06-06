n, k = map(int, input().split())
candy = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append((p, c))

candy.sort()
answer = 0
j = 0
# print(candy)
candy_sum = 0
for i in range(n):
    while j < n and candy[j][0] - candy[i][0] <= 2 * k:
        # print(f'candy[j]={candy[j]}, candy[i]={candy[i]}')
        candy_sum += candy[j][1]
        j += 1
    
    answer = max(answer, candy_sum)

    candy_sum -= candy[i][1]

print(answer)
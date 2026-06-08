n, k = map(int, input().split())
candy = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append((p, c))

candy.sort()
candy = [(-1, -1)] + candy
answer = 0
j = 0
candy_sum = 0
for i in range(1, n + 1):
    while j + 1 <= n and candy[j + 1][0] - candy[i][0] <= 2 * k:
        candy_sum += candy[j + 1][1]
        
        j += 1
    
    answer = max(answer, candy_sum)

    candy_sum -= candy[i][1]

print(answer)

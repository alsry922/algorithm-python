n, k = map(int, input().split())
candy = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append((p, c))

# Please write your code here.
# 바구니 위치를 기준으로 정렬
candy.sort()
candy = [(-1, -1)] + candy
# j를 0부터 시작해서 j 바구니의 위치가 i 바구니의 위치 +  (2 * k) 이내면 j를 증가시킴
j = 0
csum = 0
answer = 0
for i in range(1, n + 1):
    while j + 1 <= n and candy[j + 1][0] <= candy[i][0] + 2 * k:
        csum += candy[j + 1][1]
        j += 1
    
    answer = max(answer, csum)

    csum -= candy[i][1]

print(answer)

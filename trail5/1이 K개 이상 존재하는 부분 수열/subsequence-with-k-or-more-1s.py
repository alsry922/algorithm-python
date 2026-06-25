n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 투 포인터 사용 가능?
# i, j 투 포인터를 잡았을 때, i가 증가하면 j도 유지되거나 증가되어야 함.
j = 0
cnt = 0 # 1의 갯수
answer = float('inf')
for i in range(1, n + 1):
    while j + 1 <= n and cnt < k:
        if arr[j + 1] == 1:
            cnt += 1
        j += 1
    
    # 끝까지 봤는데 1이 k개 이상일 수가 없음
    if cnt < k:
        break

    answer = min(answer, j - i + 1)

    if arr[i] == 1:
        cnt -= 1

print(-1 if answer == float('inf') else answer)
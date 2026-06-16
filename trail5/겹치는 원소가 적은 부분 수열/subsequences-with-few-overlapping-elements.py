from collections import defaultdict
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 투 포인터 사용 가능
# i, j 투 포인터 i 가 증가했을 때 뽑은 원소 하나가 사라지는 것이기 때문에
# j를 증가시켜 새로운 원소를 뽑아 길이를 더 길게 만들 수 있음
# j + 1(다음 수)가 범위 안에 있고, 현재 k개 미만인 경우 뽑을 수 있음.
# 반복하며 j를 증가시키다가 조건을 만족시키지 못하는 경우, loop 탈출
# j가 끝까지 이동했으면(모든 수를 다 살펴본 경우) outer loop break
#   이 구간이 답이므로
# j가 아직 남은 경우에 조건이 만족된 경우는 answer를 갱신

count = defaultdict(int)
answer = 1
j = 0
for i in range(1, n + 1):
    while j + 1 <= n and count[arr[j + 1]] < k:
        count[arr[j + 1]] += 1
        j += 1
    
    answer = max(answer, j - i + 1)

    if j == n:
        break
    
    count[arr[i]] -= 1

print(answer)
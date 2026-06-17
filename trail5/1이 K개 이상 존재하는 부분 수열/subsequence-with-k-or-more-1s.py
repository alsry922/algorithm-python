n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 조건에 맞는 연속 부분 수열 구하기
# 연속 부분 수열 -> 슬라이딩 윈도우
# 가장 짧은 구간 찾기 -> 가변 윈도우
# 투 포인터 i, j 사용 가능?
#   i를 왼쪽 j를 오른쪽 포인터로 설정했을 때, i가 증가하면 1이 하나 줄어들 수 있으니까
#   조건을 만족시키기 위해서 j가 뒤로갈 필요가 없음
#   단조성 확인되므로 투 포인터 사용 가능

# while문을 반복하며 다음 위치(j + 1)가 범위 안에 존재하며,
# 지금까지 뽑은 1의 갯수가 k 미만인 경우 반복 가능
# while loop 탈출하고 길이 계산 후 답을 갱신
# 다음 loop 진입 전에 i번째 수가 1인 경우 1 count 변수 감소시켜야 함.
# 그리고 i를 증가시킴
MIN = float('inf')
answer = MIN
j = 0
count = 0
for i in range(1, n + 1):
    while j + 1 <= n and count < k:
        if arr[j + 1] == 1:
            count += 1
        j += 1

    if count < k:
        break

    answer = min(answer, j - i + 1)

    if arr[i] == 1:
        count -= 1

print(-1 if answer == MIN else answer)

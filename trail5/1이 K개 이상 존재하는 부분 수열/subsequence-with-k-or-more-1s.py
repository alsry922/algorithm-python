n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 가장 짧은 연속 부분 수열 -> 가변 슬라이딩 윈도우
# 투 포인터 i, j 사용 가능 여부
#   i가 증가할 때 1이 줄어들 수 있음.
#   K개 이상 존재하기 위해서는 j를 뒤로 돌릴 수 없음.
#   j 또한 증가시켜서 1을 찾아야 함.
#   단조성 확인을 사용 가능
# while문을 반복하며 j를 증가
#   j + 1이 범위 안에 있고, 지금까지 고른 1의 갯수가 K개 미만이면
#   j + 1 위치의 수를 뽑을 수 있음.
#   뽑은 수가 1이라면 1의 갯수를 증가시키고
#   j도 증가시킴
# while loop 탈출
#   조건이 맞지 않아 탈출하게 되는 경우
#   j - i + 1로 길이를 계산하여 답을 갱신함.
j = 0
count = 0
MIN = float('inf')
answer = MIN
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
n, k = map(int, input().split())
candy = []
for _ in range(n):
    c, p = map(int, input().split())
    candy.append((p, c))

candy.sort()
# Please write your code here.
# c를 기준으로 [c - k, c + k] 구간의 모든 사탕 수를 탐색했을 때 최대를 출력
# 구간 탐색
#   슬라이딩 윈도우
# 바구니 위치를 기준으로 정렬
# 투 포인터 사용 가능한가?
#   바구니를 가리키는 i, j 투 포인터를 뒀을 때, i가 증가하게 되면 사탕 총 갯수가 줄어들게 되므로 j를 감소시켜서는 안됨.
#   i, j가 한 방향으로만 이동할 수 있는 단조성 확보
#   투 포인터 사용 가능
# 다음에 볼 바구니(A)가 전체 범위 안에 있으며, A와 시작 바구니(B)의 위치가 2 * k 거리 내에 있는 경우
#   현재까지의 사탕 수의 합에 다음에 볼 바구니 A의 사탕 수도 더하여 갱신.
# A를 뽑을 수 없는 상황이면 반복문을 빠져나와 답을 갱신하고, i번째 바구니의 사탕 갯수를 합에서 제외함.

j = 0
csum = candy[0][1]
answer = 0
for i in range(n):
    # 다음에 볼 바구니(A)가 전체 범위 안에 있으며, A와 시작 바구니(B)의 위치가 2 * k 거리 내에 있는 경우
    while j + 1 < n and candy[j + 1][0] - candy[i][0] <= 2 * k:
        # 뽑기
        csum += candy[j + 1][1]
        j += 1
    
    answer = max(answer, csum)

    csum -= candy[i][1]

print(answer)
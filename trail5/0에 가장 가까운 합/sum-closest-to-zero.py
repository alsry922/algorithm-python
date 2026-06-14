n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
# 두 개 위치를 골라 두 원소의 합 중 0에 가장 가까운 값을 절댓값으로 출력
# 두 개의 위치를 고르는 문제 -> 투 포인터 사용 가능?
#   a를 정렬
#   i, j 투 포인터 설정(시작, 끝)
#   a[i] + a[j] 값이 0보다 큰 경우 j를 감소
#   a[i] + a[j] 값이 0보다 작은 경우 i를 증가
#   i, j 둘 다 한 방향으로만 이동 -> 단조성 확인, 투 포인터 사용 가능
# i < j 일 때까지 i, j 이동을 반복
#   a[i] + a[j] 의 합의 절댓값이 0에 가까울수록 답을 갱신
a.sort()
def solution():
    j = n - 1
    i = 0
    answer = float('inf')
    while i < j:
        answer = min(answer, abs(a[i] + a[j]))
        if a[i] + a[j] < 0:
            i += 1
        elif a[i] + a[j] > 0:
            j -= 1
        else:
            return 0
            
    return answer

print(solution())
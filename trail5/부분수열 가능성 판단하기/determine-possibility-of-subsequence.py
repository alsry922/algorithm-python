n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

# Please write your code here.
# 투 포인터 i, j 사용 가능?
# j를 0부터 순회 시작
    # A[j] == B[i] 매칭되었을 때, 다음 매칭되는 수를 찾기 위해서는
    # i + 1, j + 1 부터 찾아야 함.
    # i가 증가하면 j도 증가할 수 밖에 없음.
    # 단조성 확인
# B에서 하나씩 지울 때마다 B가 A의 부분 수열인지 확인하면 정답을 찾을 수 있음.
# 하지만, 이렇게 하면 O(NM) 시간복잡도로 시간초과가 발생하게 됨.
# B에서 하나씩 지운 결과가 A의 부분 수열인지 O(1) 만에 확인할 수 있는 방법이 있나?
# L,R 테크닉 사용
# L[i] = B[i] 가 A[1 ... j]에서 가장 마지막으로 등장하는 인덱스
# R[i] = B[i] 가 A[j ... n - 1]에서 가장 마지막으로 등장하는 인덱스
L = [0] * (m + 2)
R = [0] * (m + 2)

j = 1
for i in range(1, m + 1):
    # j + 1 이 범위 안에 있고, A[j + 1] 과 B[i]가 다르면 j를 증가시킴
    while j <= n and A[j] != B[i]:
        j += 1
    L[i] = j

j = n
for i in range(m, 0, -1):
    while j >= 1 and A[j] != B[i]:
        j -= 1
    R[i] = j

answer = 0
L[0] = 0
R[m + 1] = n + 1

for i in range(1, m + 1):
    if L[i - 1] < R[i + 1]:
        answer += 1

print(answer)

# Please write your code here.
# B의 특정 위치의 원소를 지웠을 때의 수열이 A의 부분수열이 되는 가짓수를 출력.
# B가 A의 부분수열인지 찾기
#   나이브하게 단순히 B의 첫 번쨰 원소가 A에 등장하는 위치(i)를 찾음
#   B의 두 번째 원소가 A에 등장하는 위치(j)를 i + 1부터 찾음
#   B의 세 번쨰 원소가 A에 등장하는 위치(k)를 j + 1부터 찾음
# B의 각 원소를 A에서 찾을 때, 
# 이전 원소를 찾은 위치 이후부터 처음 등장하는 위치를 알면,
# 부분 수열인지 아닌지 알 수 있음.
# L[i] = L[i - 1] + 1 위치부터 B[i] 가 등장하는 최초의 A의 인덱스
# R[i] = R[i + 1] - 1 위치부터 B[i] 가 등장하는 최초의 A의 인덱스
# B[i]를 지웠을 때 B가 A의 부분 수열이 되는지 판단을 위해서는 L[i - 1] < R[i + 1] 인지 확인하면 됨
# L, R 을 구하기 위해 투 포인터(i, j) 사용 가능?
#   i는 B를 가리키고 A는 j를 가리키는 방식 투 포인터를 사용하면
#   L의 정의에 따라 i와 j를 한 방향으로만 이동함.
#   단조성이 확인되므로 사용 가능

# L 구하기
# while문을 반복
# i는 B를 가리키고 j는 A를 가리키킴
# j 가 A 인덱스 범위 안에 있고, B[i] != A[j]인 경우에만,
# loop를 돌며 j += 1을 함
# B[i] == A[j] 인 경우 while loop를 탈출하며 A의 인덱스를 L[i]에 기록
# 찾은 A 인덱스 다음 위치부터 찾아야 하니까 j += 1을 한 번 더 수행
# i도 증가시키고 while loop를 재진입

# R 구하기도 마찬가지
n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

L = [0] * (m + 2)
R = [0] * (m + 2)
L[0] = -1
R[m + 1] = n + 1
j = 1
for i in range(1, m + 1):
    # j가 범위안에 있고 B[i] != A[j] 인 경우는 반복 가능
    while j <= n and B[i] != A[j]:
        j += 1
    L[i] = j
    if j <= n:
        j += 1

j = n
for i in range(m, 0, -1):
    while j >= 0 and B[i] != A[j]:
        j -= 1
    R[i] = j
    if j >= 0:
        j -= 1

answer = 0
for i in range(1, m + 1):
    if L[i - 1] < R[i + 1]:
        answer += 1
    
print(answer)
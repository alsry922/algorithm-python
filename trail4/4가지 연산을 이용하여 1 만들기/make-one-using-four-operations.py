from collections import deque
from collections import defaultdict
N = int(input())
calc = [1, 1, 2, 3]
visited = defaultdict(bool)
q = deque()
# Please write your code here.
# 1더하기, 1빼기, 2나누기, 3나누기
# 그리디가 가능한가?
#   1로 만들기 위해서는 매 연산마다 숫자를 줄이는 게 좋음.
#   하지만 예시처럼 1을 더한 후에 숫자를 줄이는 경우가 더 최적해인 경우가 발생함.
#   그리디로는 안될 것 같음.

# dp는?
# dp도 불가능 할 것 같음.
# 부분 문제로 나눌 수 있는지 모르겠음.
#   마지막인 1이 되기 위해서 2에서 1을 빼거나 2를 나누거나 3에서 3을 나누거나 0에서 1을 더하는 경우임.
#   애초에 0이 되는 경우는 존재하지 않을 것임.
#   그럼 결론적으로 2에서 1을 빼는 경우, 2에서 2를 나누는 경우, 3에서 3을 나누는 경우의 부분문제로 나눌 수 있음.
#   이런 부분 문제의 결과 값이 상위 문제 해결을 위해 계속해서 사용되는가?
#   사용되도록 할 수 있을 것 같음.
#   하지만 dp 정의가 너무 어려움.
#   dp[i] = i가 되기 이전의 수에서 i가 되기위한 연산의 수
#   dp[i] = dp[i+1] - 1, dp[i-1] + 1, dp[i*2] + 1, dp[i*3] + 1
#   이렇게 할 수 있을 것 같은데 초기값 설정이 안될 것 같음.
#   이 방법은 모르겠음.

# bfs는?
#   덧셈, 뺄셈, 2나눗셈, 3나눗셈이 상하좌우 이동처럼 갈 수 있는 방향이 된다.
#   그런데 문제는 1더하기로 이동 시에 갈 수 있는 수가 무한이어서 queue에 계속 추가됨
#   이러면 반복문을 종료할 수 있나?
#   이러나 저러나 저 4가지 연산으로 1이될 수 있는 방법은 무조건 존재함.
#   그리고 bfs를 사용하면 같은 시작점에서 같은 레벨로 시작하니까 먼저 1에 도달한 경우가 생기면
#   그게 최소 연산 횟수가 되고 정답이 됨.
#   따라서 1을 계속 더해서 무한 루프가 될 가능성은 없음.
#   가능한 연산을 사용하여 만든 수를 계속 queue에 삽입해서
#   queue에 삽입할 수가 1이되는 순간의 연산 횟수(cnt)를 print 하면 될 것 같음.

def can_go(num):
    return not visited[num] and num >= 1

def push(num, count):
    visited[num] = True
    q.append((num, count))

def bfs(snum):
    push(snum, 0)
    while q:
        cnum, count = q.popleft()
        if cnum == 1:
            return count
        if cnum % 3 == 0 and can_go(cnum // 3):
            push(cnum // 3, count + 1)
        if cnum % 2 == 0 and can_go(cnum // 2):
            push(cnum // 2, count + 1)
        if can_go(cnum - 1):
            push(cnum - 1, count + 1)
        if can_go(cnum + 1):
            push(cnum + 1, count + 1)
answer = bfs(N)
print(answer)
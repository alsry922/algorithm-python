from sortedcontainers import SortedSet
n = int(input())

segments = [ tuple(map(int, input().split())) for _ in range(n) ]
# Please write your code here.
segments.sort()
covered = SortedSet()
cnt = 0
for y, x1, x2 in segments:
    checkIdx = covered.bisect_right(( x1, x2 )) - 1
    # 나보다 앞에 있는 선분이 있고, 앞 선분과 완전히 겹치는 경우는 아무것도 안함.
    if checkIdx >= 0:
        cx1, cx2 = covered[checkIdx]
        if cx1 <= x1 and x2 <= cx2:
            continue
    
    # 위의 경우를 제외하고는 무조건 보임
    cnt += 1
    mx1 = x1
    mx2 = x2
    # 지워질 선분들 관리(현재 선분과 병합될 선분들)
    to_remove = []
    for i in range(max(0, checkIdx), len(covered)):
        cx1, cx2 = covered[i]
        if cx1 > x2:
            break
        if not(cx1 > x2 or cx2 < x1):
            mx1 = min(mx1, cx1)
            mx2 = max(mx2, cx2)
            to_remove.append((cx1, cx2))
    
    for ele in to_remove:
        covered.remove(ele)
    
    covered.add((mx1, mx2))
    
print(cnt)
from sortedcontainers import SortedSet
n = int(input())
segments = []
for _ in range(n):
    yi, x1i, x2i = map(int, input().split())
    segments.append((yi, x1i, x2i))
    

# Please write your code here.
# y값이 작은 순으로 정렬
segments.sort()
covered = SortedSet()
cnt = 0
for y, x1, x2 in segments:
    # 완전히 겹치는 경우는 제외
    checkIdx = covered.bisect_right((x1, x2)) - 1
    if checkIdx >= 0:
        cx1, cx2 = covered[checkIdx]
        if cx1 <= x1 and x2 <= cx2:
            continue
    
    # 완전히 겹치는 경우가 아니면 선분이 보임
    cnt += 1
    # 현재 선분과 겹치는 선분이 존재하는지 확인
    to_remove = []
    mx1, mx2 = x1, x2
    for i in range(max(0, checkIdx), len(covered)):
        cx1, cx2 = covered[i]
        if cx1 > x2:
            break
        if not (cx2 < x1) and not (x2 < cx1):
            to_remove.append((cx1, cx2))
            mx1 = min(mx1, cx1)
            mx2 = max(mx2, cx2)
    # 겹치는 선분을 병합하여 하나의 선분으로 만듦
    for ele in to_remove:
        covered.remove(ele)
    covered.add((mx1, mx2))
print(cnt)
from sortedcontainers import SortedSet
n = int(input())
segments = []
for _ in range(n):
    yi, x1i, x2i = map(int, input().split())
    segments.append((yi, x1i, x2i))

# Please write your code here.
segments.sort()
covered = SortedSet()
cnt = 0

for y, x1, x2 in segments:
    # 1. 완전히 가려지는지 체크
    checkIdx = covered.bisect_right((x1, x2)) - 1
    if checkIdx >= 0:
        cx1, cx2 = covered[checkIdx]
        if cx1 <= x1 and x2 <= cx2:
            continue
    
    # 2. 겹치는 구간 수집 후 머지
    cnt += 1
    new_x1, new_x2 = x1, x2
    to_remove = []
    for idx in range(max(0, checkIdx), len(covered)):
        cx1, cx2 = covered[idx]
        if cx1 > x2:
            break
        if (x1 <= cx1 <= x2) or (cx1 <= x1 <= cx2):
            new_x1 = min(cx1, new_x1)
            new_x2 = max(cx2, new_x2)
            to_remove.append((cx1, cx2))
    
    for ele in to_remove:
        covered.remove(ele)
    covered.add((new_x1, new_x2))

print(cnt)
import sys
input = sys.stdin.readline
n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*intervals)
a, b = list(a), list(b)

# Please write your code here.
points = []
for index, (x1, x2) in enumerate(zip(a, b)):
    points.append((x1, +1, index + 1))
    points.append((x2, -1, index + 1))

points.sort()
count = 0
start = -1
max_seg_leng = -1
for x, v, num in points:
    if v == 1:
        # if not seg:
        if count == 0:
            start = x
        # seg.add(num)  
        count += 1
    else:
        end = x
        # seg.remove(num)
        count -= 1
        if count == 0:
            max_seg_leng = max(max_seg_leng, end - start)

print(max_seg_leng)

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# 길이
# 지워진 수
from sortedcontainers import SortedSet, SortedDict
ss = SortedSet([-1, n+1])
sm = SortedDict()
sm[n+2] = 1
for num in nums:
    s, e = ss[ss.bisect_left(num) - 1], ss[ss.bisect_left(num)]
    ss.add(num)
    sm[e-s] -= 1
    if sm[e-s] == 0:
        del sm[e-s]
    if (num - s) in sm:
        sm[num-s] += 1
    else:
        sm[num-s] = 1
    if (e-num) in sm:
        sm[e-num] += 1
    else:
        sm[e-num] = 1
    print(max(sm) - 1)
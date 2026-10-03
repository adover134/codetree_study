n, m = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# 길이, 시작, 끝
# 지워진 수
from sortedcontainers import SortedSet
ss1 = SortedSet([-1, n + 1])
ss2 = SortedSet([(-n - 1, -1, n + 1)])
maxi = 0
for num in nums:
    s = ss1[ss1.bisect_right(num) - 1]
    e = ss1[ss1.bisect_right(num)]
    ss1.add(num)
    ss2.remove((-(e - s - 1), s, e))
    ss2.add((-(num - s - 1), s, num))
    ss2.add((-(e - num - 1), num, e))
    print(-ss2[0][0])


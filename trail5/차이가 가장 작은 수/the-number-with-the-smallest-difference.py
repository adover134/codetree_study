n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(arr)
mini = 2000000001
for i in range(len(ss) - 1):
    a = ss[i]
    t = ss.bisect_left(a + m)
    if t == len(ss):
        break
    mini = min(ss[t] - a, mini)
if mini == 2000000001:
    print(-1)
else:
    print(mini)
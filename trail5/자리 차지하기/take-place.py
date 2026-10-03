n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(range(1, m + 1))
ans = 0
for q in a:
    t = ss.bisect_right(q)
    if t == 0:
        break
    else:
        ss.remove(ss[t - 1])
    ans += 1
print(ans)
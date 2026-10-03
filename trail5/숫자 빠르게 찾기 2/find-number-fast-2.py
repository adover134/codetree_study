n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(arr)
for q in queries:
    t = ss.bisect_left(q)
    if t == n:
        print(-1)
    else:
        print(ss[t])
n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(points)
for q in queries:
    t = ss.bisect_left((q, 0))
    if t == len(ss):
        print(-1, -1)
    else:
        x, y = ss[t]
        ss.remove((x, y))
        print(x, y)
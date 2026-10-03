n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(points)
for q in queries:
    t = ss.bisect_right(q)
    if t == len(ss):
        print(-1, -1)
    else:
        a, b = ss[t]
        print(a, b)
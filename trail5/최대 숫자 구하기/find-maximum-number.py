n, m = map(int, input().split())
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet([i+1 for i in range(m)])
for q in queries:
    ss.remove(q)
    print(ss[-1])
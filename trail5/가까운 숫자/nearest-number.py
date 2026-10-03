n = int(input())
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet([0])
mini = 1000000001
for q in queries:
    ss.add(q)
    t = ss.bisect_left(q)
    if t > 0:
        mini = min(mini, ss[t] - ss[t - 1])
    if t < len(ss) - 1:
        mini = min(mini, ss[t + 1] - ss[t])
    print(mini)
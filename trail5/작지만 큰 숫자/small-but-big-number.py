n, m = map(int, input().split())
sequence = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(sequence)
ans = []
for q in query:
    if len(ss) == 0:
        ans.append(-1)
    else:
        t = ss.bisect_left(q)
        if t == len(ss):
            ans.append(ss[-1])
            ss.remove(ss[-1])
        elif ss[t] > q and t > 0:
            ans.append(ss[t-1])
            ss.remove(ss[t-1])
        elif ss[t] == q:
            ans.append(ss[t])
            ss.remove(ss[t])
        else:
            ans.append(-1)
for num in ans:
    print(num)
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(arr)
for i in range(k):
    print(ss[-i - 1], end = ' ')
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedDict
sd = SortedDict()
for i, num in enumerate(arr):
    if num not in sd:
        sd[num] = i
for k, v in sd.items():
    print(k, v + 1)
N, G = map(int, input().split())

group = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.
from collections import deque
from copy import deepcopy
group = deque([set(g) for g in group])
found = {1}
while group:
    f = len(group)
    for _ in range(len(group)):
        g = group.popleft()
        if len(g-found) == 1:
            found = found.union(g)
            f = True
        else:
            group.append(g)
    if f == len(group):
        break
print(len(found))
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
found = [[] for i in range(n + 1)]
visited = set([1])
for edge in edges:
    found[edge[0]].append(edge[1])
    found[edge[1]].append(edge[0])
from collections import deque
dq = deque([1])
while dq:
    x = dq.popleft()
    for p in found[x]:
        if p not in visited:
            visited.add(p)
            dq.append(p)
print(len(visited) - 1)
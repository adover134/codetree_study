n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
dq = deque([(0, 0)])
visited = set([(0, 0)])
while dq:
    r, c = dq.popleft()
    if r == (n - 1) and c == (m - 1):
        break
    if c < (m - 1):
        if grid[r][c + 1] == 1 and (r, c + 1) not in visited:
            visited.add((r, c+ 1))
            dq.append((r, c + 1))
    if r < (n - 1):
        if grid[r + 1][c] == 1 and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            dq.append((r + 1, c))
if (n - 1, m - 1) in visited:
    print(1)
else:
    print(0)
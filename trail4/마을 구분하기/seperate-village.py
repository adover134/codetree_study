n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
sizes = []
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            dq = deque([(y, x)])
            grid[y][x] = 0
            s = 1
            while dq:
                r, c = dq.popleft()
                for d in range(4):
                    ar, ac = r + dr[d], c + dc[d]
                    if ar < 0 or ar >= n or ac < 0 or ac >= n:
                        continue
                    if grid[ar][ac] == 0:
                        continue
                    dq.append((ar, ac))
                    grid[ar][ac] = 0
                    s += 1
            sizes.append(s)
print(len(sizes))
for size in sorted(sizes):
    print(size)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
maxi, cnt = 0, 0
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

for r in range(n):
    for c in range(n):
        if grid[r][c] != 0:
            tc = 1
            target = grid[r][c]
            grid[r][c] = 0
            dq = deque([(r, c)])
            while dq:
                R, C = dq.popleft()
                for d in range(4):
                    ar, ac = R + dr[d], C + dc[d]
                    if ar < 0 or ar >= n or ac < 0 or ac >= n:
                        continue
                    if grid[ar][ac] == target:
                        dq.append((ar, ac))
                        grid[ar][ac] = 0
                        tc += 1
            if tc >= 4:
                cnt += 1
            if maxi < tc:
                maxi = tc
print(cnt, maxi)
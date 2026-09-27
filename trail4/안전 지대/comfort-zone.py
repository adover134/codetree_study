n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque
from copy import deepcopy
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

def find_safe(h, grid):
    cnt = 0
    M = deepcopy(grid)
    for r in range(n):
        for c in range(m):
            if M[r][c] > h:
                cnt += 1
                M[r][c] = 0
                dq = deque([(r, c)])
                while dq:
                    R, C = dq.popleft()
                    for d in range(4):
                        ar, ac = R + dr[d], C + dc[d]
                        if ar < 0 or ar >= n or ac < 0 or ac >= m:
                            continue
                        if M[ar][ac] > h:
                            M[ar][ac] = 0
                            dq.append((ar, ac))
    return cnt

maxi = -1
mini = 100

for i in range(1, 100):
    cnt = find_safe(i, grid)
    if maxi < cnt:
        maxi = cnt
        mini = i

print(mini, maxi)
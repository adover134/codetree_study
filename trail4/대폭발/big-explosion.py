n, m, r, c = map(int, input().split())

# Please write your code here.
from collections import deque
r, c = r - 1, c - 1
dq = deque([(r, c)])
bombs = set([(r, c)])
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
for t in range(m):
    while dq:
        r, c = dq.popleft()
        for d in range(4):
            ar, ac = dr[d] * (2 ** t) + r, dc[d] * (2 ** t) + c
            if ar < 0 or ac < 0 or ar >= n or ac >= n:
                continue
            else:
                bombs.add((ar, ac))
    dq = deque(list(bombs))
print(len(bombs))
n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.
from collections import deque
dq = deque([])
for i in range(m):
    dq.append((r[i] - 1, c[i] - 1))
    
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
for T in range(t):
    temp = set()
    found = set()
    for _ in range(len(dq)):
        r, c = dq.popleft()
        cur = 0
        tr, tc = 0, 0
        for d in range(4):
            ar, ac = r + dr[d], c + dc[d]
            if ar < 0 or ar >= n or ac < 0 or ac >= n:
                continue
            if a[ar][ac] > cur:
                tr, tc = ar, ac
                cur = a[ar][ac]
        if (tr, tc) in found:
            if (tr, tc) in temp:
                temp.remove((tr, tc))
        else:
            temp.add((tr, tc))
            found.add((tr, tc))
    dq = deque(list(temp))
print(len(dq))

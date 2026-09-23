N, M, K = map(int, input().split())

x, y = [], []
for _ in range(M):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d, p = [], []
for _ in range(K):
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))

# Please write your code here.
from collections import deque
dq = deque([(0, 0)])
apples = set(zip(x, y))
dx, dy = {'U': -1, 'D': 1, 'L': 0, 'R': 0}, {'U': 0, 'D': 0, 'L': -1, 'R': 1}
failed = False
t = 0
x, y = 0, 0
for dir, pos in zip(d, p):
    for i in range(pos):
        t += 1
        tx, ty = dq.popleft()
        ax, ay = x + dx[dir], y + dy[dir]
        if ax < 0 or ay < 0 or ax >= N or ay >= N:
            failed = True
            break
        if (ax, ay) in dq:
            failed = True
            break
        x, y = ax, ay
        dq.append((x, y))
        if (x + 1, y + 1) in apples:
            apples.remove((x + 1, y + 1))
            dq.appendleft((tx, ty))
    if failed:
        break
print(t)
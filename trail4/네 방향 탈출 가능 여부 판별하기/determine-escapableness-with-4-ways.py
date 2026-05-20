n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[False for i in range(m)] for j in range(n)]
from collections import deque
dq=deque([(0,0)])
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited[0][0]=True
while dq:
    x,y=dq.popleft()
    for d in range(4):
        ax,ay=x+dx[d],y+dy[d]
        if ax<0 or ax>=n or ay<0 or ay>=m:
            continue
        elif a[ax][ay]==0:
            continue
        elif visited[ax][ay]:
            continue
        else:
            dq.append((ax,ay))
            visited[ax][ay]=True
            if ax==n and ay==m:
                break
if visited[n-1][m-1]:
    print(1)
else:
    print(0)
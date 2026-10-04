n, t = map(int, input().split())
start = []
speed = []

for _ in range(n):
    s, v = map(int, input().split())
    start.append(s)
    speed.append(v)

# Please write your code here.
# N명이 있고
# T 분 동안 달리며
# 두 사람이 만나면 둘의 속도가 같아져야 한다.
# (속도, 위치)가 있고
# 매 루프마다 위치 만 있는 걸 만들면 되지 않을까?
# 속도가 느린 사람이 먼저 오면 될 거야.
ps = dict(zip(start, speed))
p = sorted(start, reverse = True)
ans = 0
d = 1000000000*1000000000+1
for pos in p:
    r = pos + ps[pos]*t
    if d > r:
        d = r
        ans += 1
print(ans)
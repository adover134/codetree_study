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
from sortedcontainers import SortedSet
# 위치와 속도를 가진다.
# 위치 순으로 먼저 정렬되어야 한다.
sp = sorted([(-start[i], -speed[i]) for i in range(n)])
# 위치가 더 작은데 속도도 더 작다면
# 절대 못 만난다.
# 즉, 더 앞쪽의 누군가보다 더 빠르다면
# 그 사람은 결국 그룹에 속한다.

# 가장 멀리 있는 사람부터 출발해서
# 다음의 누군가가 자기보다 앞에 도착한다면 그 사람의 도착 예정 위치는 집합에 안 넣는다.

# 더 멀리 있고, 더 빠른 사람부터 집합에 넣어야 한다.
pos = 1000000000+1000000000000000000
ans = 0
for i in range(len(sp)):
    s, v= sp[i]
    r = -(s+(v * t))
    if r >= pos:
        continue
    else:
        ans += 1
        pos = r

print(ans)
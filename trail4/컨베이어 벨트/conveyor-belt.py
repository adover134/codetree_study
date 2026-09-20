n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# n초마다 위아래가 바뀌며
# 2n초 후에는 원래 상태가 된다.
t %= 2*n
if t >= n:
    t -= n
    u, d = d, u
if t > 0:
    for num in d[-t:]+u[:-t]:
        print(num, end=' ')
    print()
    for num in u[-t:]+d[:-t]:
        print(num, end=' ')
else:
    for num in u:
        print(num, end=' ')
    print()
    for num in d:
        print(num, end=' ')

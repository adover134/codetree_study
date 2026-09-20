n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
from collections import deque
for line, direction in winds:
    line -= 1
    if direction == 'L':
        dq = deque([(line, 1)])
    else:
        dq = deque([(line, 0)])
    while dq:
        l, d = dq.popleft()
        if d == 1:
            a[l] = [a[l][-1]]+a[l][:-1]
        else:
            a[l] = a[l][1:]+[a[l][0]]
        if l <= line and l > 0:
            f = False
            for ori, ne in zip(a[l], a[l-1]):
                if ori == ne:
                    f = True
                    break
            if f:
                dq.append((l-1, 1-d))
        if l >= line and l < (n-1):
            f = False
            for ori, ne in zip(a[l], a[l+1]):
                if ori == ne:
                    f = True
                    break
            if f:
                dq.append((l+1, 1-d))

for line in a:
    for num in line:
        print(num, end=' ')
    print()
n = int(input())
P, L = [], []
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet(list(zip(L, P)))
for cmd in commands:
    match cmd[0]:
        case 'rc':
            if cmd[1] == 1:
                print(ss[-1][1])
            else:
                print(ss[0][1])
        case 'ad':
            ss.add((cmd[2], cmd[1]))
        case 'sv':
            ss.remove((cmd[2], cmd[1]))
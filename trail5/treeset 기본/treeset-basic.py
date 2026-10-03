n = int(input())
command = []
x = []

for _ in range(n):
    line = input().split()
    command.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)

# Please write your code here.
from sortedcontainers import SortedSet
ss = SortedSet()
for cmd, val in zip(command, x):
    match cmd:
        case 'add':
            ss.add(val)
        case 'remove':
            ss.remove(val)
        case 'find':
            if val in ss:
                print('true')
            else:
                print('false')
        case 'lower_bound':
            t = ss.bisect_left(val)
            if t == len(ss):
                print('None')
            else:
                print(ss[t])
        case 'upper_bound':
            t = ss.bisect_right(val)
            if t == len(ss):
                print('None')
            else:
                print(ss[t])
        case 'largest':
            if len(ss) > 0:
                print(max(ss))
            else:
                print('None')
        case 'smallest':
            if len(ss) > 0:
                print(min(ss))
            else:
                print('None')
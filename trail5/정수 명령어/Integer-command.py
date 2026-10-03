T = int(input())
from sortedcontainers import SortedSet
for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    command = [op[0] for op in operations]
    n = [int(op[1]) for op in operations]

    # Please write your code here.
    ss = SortedSet()
    for co, val in zip(command, n):
        match co:
            case 'I':
                ss.add(val)
            case 'D':
                if len(ss) == 0:
                    continue
                if val == 1:
                    ss.remove(ss[-1])
                else:
                    ss.remove(ss[0])
    if len(ss) == 0:
        print('EMPTY')
    else:
        print(max(ss), min(ss))
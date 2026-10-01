n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.
from sortedcontainers import SortedDict
treemap = SortedDict()
for c, k, v in zip(cmd, k, v):
    match c:
        case 'add':
            treemap[k] = v
        case 'remove':
            if k in treemap:
                treemap.pop(k)
        case 'find':
            if k in treemap:
                print(treemap[k])
            else:
                print('None')
        case 'print_list':
            if treemap:
                for K, V in treemap.items():
                    print(V, end = ' ')
                print()
            else:
                print('None')

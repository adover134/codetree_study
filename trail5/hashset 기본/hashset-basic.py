n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

# Please write your code here.
hs = set()
for cmd, val in zip(commands, x):
    match cmd:
        case 'add':
            hs.add(val)
        case 'remove':
            hs.remove(val)
        case 'find':
            if val in hs:
                print('true')
            else:
                print('false')
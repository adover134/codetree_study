n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
hashmap = dict()
for cmd in commands:
    match cmd[0]:
        case 'add':
            k, v = cmd[1], cmd[2]
            hashmap[k] = v
        case 'remove':
            del hashmap[cmd[1]]
        case 'find':
            k = cmd[1]
            if k in hashmap:
                print(hashmap[k])
            else:
                print('None')
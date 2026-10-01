str = input()

# Please write your code here.
pos = [-1] * 26
failed = 0
a = ord('a')
ls = len(str)
for i in range(ls):
    t = ord(str[i]) - a
    if pos[t] >= 0:
        failed += 1
        pos[t] = ls + 1
    else:
        pos[t] = i
mini = ls + 1
for i in range(26):
    if pos[i] >= 0 and pos[i] < ls and pos[i] < mini:
        mini = pos[i]
if mini == (ls + 1):
    print('None')
else:
    print(str[mini])
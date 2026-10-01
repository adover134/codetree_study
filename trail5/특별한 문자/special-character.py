str = input()

# Please write your code here.
ls = len(str)
pos = [ls + 1] * 26
failed = 0
a = ord('a')
for i in range(ls):
    t = ord(str[i]) - a
    if pos[t] < ls:
        failed += 1
        pos[t] = ls + 2
    elif pos[t] == (ls + 1):
        pos[t] = i
mini = min(pos)
if mini >= (ls + 1):
    print('None')
else:
    print(str[mini])
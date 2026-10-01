n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
from sortedcontainers import SortedDict
sd = SortedDict()
lw = len(words)
for word in words:
    if word in sd:
        sd[word] += 1
    else:
        sd[word] = 1
for k, v in sd.items():
    print(k, f'{(v * 100 / lw):.4f}')
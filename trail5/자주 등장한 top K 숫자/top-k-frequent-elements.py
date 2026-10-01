n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
cnt = Counter(arr)
cnt = sorted(zip(cnt.keys(), cnt.values()), key = lambda x: [-x[1], -x[0]])
for i in range(k):
    print(cnt[i][0], end = ' ')
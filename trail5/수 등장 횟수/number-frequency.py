n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
c = Counter(arr)
for num in nums:
    if num in c:
        print(c[num], end = ' ')
    else:
        print(0, end = ' ')
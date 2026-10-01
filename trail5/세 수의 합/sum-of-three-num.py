n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# 각 숫자 별 등장 횟수
from collections import Counter
cnt = Counter(arr)
ans = 0
for i in range(n):
    num = arr[i]
    cnt[num] -= 1
    for j in range(i):
        t = (k - num - arr[j])
        if t in cnt:
            ans += cnt[t]
print(ans)
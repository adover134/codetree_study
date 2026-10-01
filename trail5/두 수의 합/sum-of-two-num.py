n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import Counter
nums = Counter(arr)
cnt = 0
h = k // 2
if k % 2 == 0:
    if (k // 2) in nums:
        t = nums[k // 2]
        cnt += t * (t - 1) // 2
        del nums[k // 2]
checked = set()
for num in nums:
    if num in checked:
        continue
    if (k - num) in nums:
        cnt += nums[num] * nums[k - num]
        checked.add(k - num)
    checked.add(num)
print(cnt)
n = int(input())

# Please write your code here.
cnt = [0] * (n+1)
cnt[0] = 1
nums = {1, 2, 5}
for i in range(1, n+1):
    for num in nums:
        if i >= num:
            cnt[i] += cnt[i-num]
    cnt[i]%=10007
print(cnt[n])
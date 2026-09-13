n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dp=[arr[0]]
for i in range(1,n):
    dp.append(max(dp[i-1]+arr[i], arr[i]))
print(max(dp))
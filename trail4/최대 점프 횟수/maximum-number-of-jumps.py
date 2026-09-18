n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dp = [-1 for _ in range(n)]
dp[0] = 0
for i in range(n):
    if dp[i] == -1:
        break
    for j in range(arr[i]):
        t = i+j+1
        if t == n:
            break
        dp[t] = dp[i]+1

print(max(dp))
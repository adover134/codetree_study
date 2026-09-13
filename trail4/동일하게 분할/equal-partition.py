n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# i번 요소를 넣었을 때
# 차이가 j인 경우가 있는가?

# offset은 100000이면 되겠어.
import sys
S = sum(arr)
if S % 2 == 1:
    print("No")
else:
    T = S//2
    dp = [False]*(T+1)
    arr=sorted(arr,reverse=True)
    for num in arr:
        if num > T:
            break
        for t in range(T,num,-1):
            if dp[t-num]:
                dp[t]=True
        dp[num]=True
    if dp[T]:
        print("Yes")
    else:
        print("No")
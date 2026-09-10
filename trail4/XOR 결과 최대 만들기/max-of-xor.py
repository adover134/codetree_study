n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
maxi = 0
def Xor(cur, tot, cnt):
    global maxi
    if cnt == m:
        maxi = max(maxi, tot)
    else:
        for i in range(cur, n):
            Xor(i+1, tot^A[i], cnt+1)
Xor(0,0,0)
print(maxi)
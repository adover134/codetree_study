N, M = map(int, input().split())

# Please write your code here.
ans = []
def pick(cur):
    global ans
    if len(ans) == M:
        for n in ans:
            print(n,end=' ')
        print()
    else:
        for i in range(cur, N):
            ans.append(i+1)
            pick(i+1)
            ans.pop()
pick(0)
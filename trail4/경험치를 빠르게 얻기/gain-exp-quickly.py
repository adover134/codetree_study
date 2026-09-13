n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 시간이 짧은 것부터 해나가며
# 경험치 합이 M을 넘는 게 생기면 종료
T = 10001
exp_=[0 for _ in range(T+1)]
quests=sorted(quests,key=lambda x:x[1])
for e, t in quests:
    for i in range(T,-1,-1):
        if exp_[i-t]>0:
            exp_[i]=max(exp_[i],(exp_[i-t]+e))
    exp_[t]=max(exp_[t],e)
for t in range(1,T+1):
    if exp_[t]>=m:
        print(t)
        break
else:
    print(-1)
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 처음에는 2개의 점을 고른 조합들을 저장하고 그 사이의 거리를 저장한다.
# 총 M개를 골라야 하며
# '최대 거리'가 갱신되려면 '최대 거리를 구성하던 두 점' 중 하나는 기준으로 남는다.
p_set = []
ans = 10001

def get_min(cur, cnt):
    global ans
    if cnt==m:
        maxi = max(
            [(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
            for i in p_set
            for j in p_set
            if i != j], default=0)
        if ans > maxi:
            ans = maxi
    else:
        for i in range(cur, n):
            p_set.append(i)
            get_min(i+1,cnt+1)
            p_set.pop()
get_min(0,0)
print(ans)
n, m, r, c = map(int, input().split())
directions = list(input().split())

# Please write your code here.
# 왼쪽으로 굴리면
# 기존에 왼쪽에 있던 수가 아래로 가고
# 위에 있던 수는 왼쪽으로
# 아래에 있던 수가 오른쪽
# 오른쪽의 수가 위로 간다.

dice = {'u': 1, 'l': 4, 'r': 3, 'f': 2, 'b': 5, 'd': 6}
ans = 0
dr = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dc = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
board = [[0 for _ in range(n +1 )] for _ in range(n + 1)]
board[r][c] = 6
for dir in directions:
    ar, ac = r + dr[dir], c + dc[dir]
    if ar <= 0 or ar > n or ac <= 0 or ac > n:
        continue
    else:
        r, c = ar, ac
    if dir == 'L':
        board[r][c] = dice['l']
        t = dice['l']
        dice['l'] = dice['u']
        dice['u'] = dice['r']
        dice['r'] = dice['d']
        dice['d'] = t
    if dir == 'R':
        board[r][c] = dice['r']
        t = dice['r']
        dice['r'] = dice['u']
        dice['u'] = dice['l']
        dice['l'] = dice['d']
        dice['d'] = t
    if dir == 'U':
        board[r][c] = dice['b']
        t = dice['b']
        dice['b'] = dice['u']
        dice['u'] = dice['f']
        dice['f'] = dice['d']
        dice['d'] = t
    if dir == 'D':
        board[r][c] = dice['f']
        t = dice['f']
        dice['f'] = dice['u']
        dice['u'] = dice['b']
        dice['b'] = dice['d']
        dice['d'] = t

print(sum(sum(row) for row in board))
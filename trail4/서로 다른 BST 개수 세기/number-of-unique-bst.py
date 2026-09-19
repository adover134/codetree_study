n = int(input())

# Please write your code here.
sub = {}
def find_tree(start, end):
    global sub
    if start > end:
        return 0
    if (start, end) not in sub:
        t = 0
        for i in range(start, end+1):
            left_sub = find_tree(start, i-1)
            right_sub = find_tree(i+1, end)
            if left_sub == 0:
                t += right_sub
            elif right_sub == 0:
                t += left_sub
            else:
                t += left_sub * right_sub
        sub[(start, end)] = max(t, 1)
    return sub[(start, end)]
print(find_tree(1, n))
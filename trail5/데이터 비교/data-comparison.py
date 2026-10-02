n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.
arr1 = set(arr1)
for num in arr2:
    print(1, end = ' ') if num in arr1 else print(0, end = ' ')
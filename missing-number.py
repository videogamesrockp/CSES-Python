N = int(input())
nums_set = set(map(int, input().split()))
 
for i in range(1, N + 1):
    if i in nums_set:
        continue
    elif i not in nums_set:
        print(i)
        break
input = list(input())

current=1
longest=1

for i in range(1,len(input)):
    if input[i]==input[i-1]:
        current+=1
    else:
        current=1
    if current>longest:
        longest=current

print(longest)
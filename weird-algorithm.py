N = int(input())
 
print(int(N), end = " ")
 
while N != 1:
    if N % 2 == 0:
        N /= 2
        print(int(N), end = " ")
    else:
        N *= 3
        N += 1
        print(int(N), end = " ")
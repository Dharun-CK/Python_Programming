#pattern1
n=int(input())
m=int(input())
for a in range(n):
    for b in range(m):
        print("@",end="  ")
    print()


#pattern2
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("$",end=" ")
    print()



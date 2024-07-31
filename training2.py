a=int(input("Enter no:"))
b=str(input("Name: "))
print(a)
print(b)
if a<40:
    if a==10:
        print("It is a Python")
    else:
        print("It is Django")
elif a<100:
    print("Take rest")
else:
    print("It is a Java")

mark = [99,80,76,56,73,190]
print(max(mark))
print(min(mark))
high = mark[0]
for i in mark:
    if high<i:
        high=i
print(high)
j=1
while j<=10:
    print("You are the best")
    j+=1
print(list(range(0,9)))

n=int(input())
m=int(input())
for a in range(n):
    for b in range(m):
        print("@",end="  ")
    print()
    

 




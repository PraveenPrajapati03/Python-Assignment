#Level 2 – Loops and basic calculations
#11
for i in range(10):
    print(i+1,end=" ")

#12
N=int(input("Enter number :"))
for i in range(N):
    print(i+1,end=" ")

#13
N=int(input("Enter number :"))
for i in range(1,N+1):
    if i%2==0:
        print(i,end=" ")

#14
N=int(input("Enter number :"))
for i in range(1,N+1):
    if i%2!=0:
        print(i,end=" ")

#15
total=0
N=int(input("Enter number :"))
for i in range(1,N+1):
    total+=i
print(total)

#16
fac=1
N=int(input("Enter number :"))
for i in range(1,N+1):
    fac*=i
print(fac)

#17
N=int(input("Enter number :"))
for i in range(1,N*10+1):
    if i%N==0:
        print(i,end=" ")

#18
count=0
N=int(input("Enter number :"))
for i in range(1,N+1):
    if i%3==0:
        count+=1
print(count)

#19
fac=1
N=int(input("Enter number :"))
for i in range(1,N+1):
    fac*=i
print(fac)

#20
N=int(input("Enter number :"))
for i in range(1,N*7+1):
    if i%7==0:
        print(i,end=" ")
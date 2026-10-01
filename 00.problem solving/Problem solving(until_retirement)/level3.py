#Level 3 – Basic number logic
#21
num=int(input("Enter number :"))
count=0
while num>0:
    num=num//10
    count+=1
print(count)

#22
num=int(input("Enter number :"))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print(sum)

#23
num=int(input("Enter number :"))
product=1
while num>0:
    digit=num%10
    product*=digit
    num=num//10
print(product)

#24
num=int(input("Enter number :"))
rnum=0
if num>0:
    while num>0:
        digit=num%10
        rnum=rnum*10+digit
        num=num//10
else:
    num=-num
    while num>0:
        digit=num%10
        rnum=rnum*10+digit
        num=num//10
    print("-",end="")
print(rnum)

#25
num=int(input("Enter number :"))
original_num=num
rnum=0
while num>0:
    digit=num%10
    rnum=rnum*10+digit
    num=num//10
if original_num==rnum:
    print("palindrome")
else:
    print("not palindrome")

#26 
num=int(input("Enter number :"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("number is prime")  
else:
    print("number is not prime") 

#27
n=int(input("Enter number :"))
for i in range(1,n+1):
    count=0
    p=1
    while p<n+1:
        if i%p==0:
            count+=1
        p+=1
    if count==2:
        print(i,end=" ")

#28
n=int(input("Enter number :"))
first=0
second=1
print(first,end=" ")
print(second,end=" ")
for a in range(1,n-1):
    third=first+second
    print(third,end=" ")
    first,second=second,third

#29
a=int(input("Enter number :"))
b=int(input("Enter number :"))
max=0
if a>b:
    max=a
else:
    max=b
gcd=0
for i in range(1,max+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd)

#30
a=int(input("Enter number :"))
b=int(input("Enter number :"))
max=0
if a>b:
    max=a
else:
    max=b
lcm=0
for i in range(max,a*b+1):
    if i%a==0 and i%b==0:
        lcm=i
        break
print(lcm)
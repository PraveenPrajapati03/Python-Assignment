#Practice Problems
#A. Basic for Loop
#1
print("Output for Question 1:.................................................")
for i in range(5):
    print("Hello")

#2
print("Output for Question 2:.................................................")
for i in range(10):
    print(i,end=" ")

#3
print("Output for Question 3:.................................................")
for i in range(1,11):
    print(i)

#4
print("Output for Question 4:.................................................")
for i in range(10,0,-1):
    print(i)

#5
print("Output for Question 5:.................................................")
for i in range(5,51,5):
    print(i)

#B. range() Practice
#6
print("Output for Question 6:.................................................")
for i in range(2,21,2):
    print(i)

#7
print("Output for Question 7:.................................................")
for i in range(1,20,2):
    print(i)

#8
print("Output for Question 8:.................................................")
for i in range(3,19,3):
    print(i,end=" ")

#9
print("Output for Question 9:.................................................")
for i in range(20,1,-2):
    print(i)

#10
print("Output for Question 10:.................................................")
n=int(input("Enter positive number:"))
for i in range(1,n+1):
    print(i)

#C. Conditions with for
#11
print("Output for Question 11:.................................................")
n=int(input("Enter positive number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

#12
print("Output for Question 12:.................................................")
n=int(input("Enter positive number:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)

#13
print("Output for Question 13:.................................................")
n=int(input("Enter positive number:"))
for i in range(1,n+1):
    if i%3==0:
        print(i)

#14
print("Output for Question 14:.................................................")
n=int(input("Enter positive number:"))
for i in range(1,n+1):
    if i%2==0 and i%3==0:
        print(i)

#15
print("Output for Question 15:.................................................")
n=int(input("Enter positive number:"))
evennumbers=0
for i in range(1,n+1):
    if i%2==0:
        evennumbers+=1
print(evennumbers)  

#D. Calculation Problems  
#16 
print("Output for Question 16:.................................................")
n=int(input("Enter positive number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)    

#17
print("Output for Question 17:.................................................")
n=int(input("Enter positive number:"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(sum)     

#18
print("Output for Question 18:.................................................")
n=int(input("Enter positive number:"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print(sum)   

#19
print("Output for Question 19:.................................................")
num=int(input("Enter number:"))
for i in range(1,11):
    print(num*i)

#20
print("Output for Question 20:.................................................")
n=int(input("Enter positive number:"))
mul=1
for i in range(1,n+1):
    mul=mul*i
print(mul)    

#E. String Iteration
#21
print("Output for Question 21:.................................................")
word=input("Enter word:")
for i in word:
    print(i)

#22
print("Output for Question 22:.................................................")
word=input("Enter word:")
for i in word:
    print(i,end="")

#23
print("Output for Question 23:.................................................")
word=input("Enter word:")
count=0
for i in word:
    count+=1
print(count)   


#24
print("Output for Question 24:.................................................")
word=input("Enter word:")
count=0
for i in range(len(word)):
    if word[i]=="a":
        count+=1
print(count)        
#or
word=input("Enter word:")
count=0
for i in word:
    if i=="a":
        count+=1
print(count)        

#25
print("Output for Question 25:.................................................")
word=input("Enter word:")
count=0
for i in word:
    if 65<=ord(i)<=91:
        count+=1
print(count)     


Practice Problems
#1
print("Output for Question 1:.................................................")
num=15
if num>10:
    print("Greater than 10")

#2
print("Output for Question 2:.................................................")    
age=19
if age>=18:
    print("Adult")

#3
print("Output for Question 3:.................................................")
num=float(input("Enter number:"))
if num>0:
    print("Number isPositive")

#4
print("Output for Question 4:.................................................")
marks=40
if marks>=40:
    print("Pass")    

#5
print("Output for Question 5:.................................................")
num=int(input("Enter number:"))
if num==0:
    print("Zero")

#6
print("Output for Question 6:.................................................")
num=1
if num>=0:
    print("Number is Positive")
else:
    print("Number is Not Positive")    

#7
print("Output for Question 7:.................................................")
user_age=int(input("Enter your age:")) 
if user_age>=18:
    print("Adult")
else:
    print("Minor")

#8
print("Output for Question 8:.................................................")
a=int(input("Enter number:"))
if a%2==0:
    print("Number is Even")
else:
    print("Number is Odd")  

#9      
print("Output for Question 9:.................................................")
marks=int(input("Enter your marks:"))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#10
print("Output for Question 10:.................................................")
a=int(input("Enter number:"))
b=int(input("Enter number:"))
if a>b:
    print("a is greater than b")        
else:
    print("b is greater than a") 

#11
print("Output for Question 11:.................................................")
marks=int(input("Enter your marks:"))
if marks>=90:
    print("A")
elif 75<=marks<=89:
    print("B")
elif 60<=marks<=74:
    print("C")
elif 40<=marks<=59:
    print("D") 
else:
    print("F")

#12
print("Output for Question 12:.................................................")
num=int(input("Enter number:"))
if num>0:
    print("Number is Positive")
elif num<0:
    print("Number is Negative")
else:
    print("Number is Zero")

#13
print("Output for Question 13:.................................................")
a=int(input("enter your choise:"))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")        
elif a==5:
    print("Friday")   
else:
    print("Other")   

#14    
print("Output for Question 14:.................................................")
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Excellent")
elif 60<=marks<=89:
    print("Good")
elif 40<=marks<=59:
    print("Pass")
else:
    print("Fail")

#15
print("Output for Question 15:.................................................")
a=int(input("enter your Number:"))
if a==1:
    print("1")
elif a==2:
    print("2")
elif a==3:
    print("3")
else :
    print("Other") 

#16
print("Output for Question 16:.................................................")      
age=int(input("Enter your age:")) 
if age>=18:
    if age<=60:
        print("Age Between 18 and 60")
    else:
        print("Age is greater than 60")        
else:
    print("Minor")      

#17
print("Output for Question 17:.................................................")
marks=int(input("Enter your marks:"))      
if marks>=40:
    if marks>=75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")

#18
print("Output for Question 18:.................................................")
num=int(input("enter your Number:"))
if num>=0:
    if num>100:
        print("Number is greater than 100")
    else:
        print("Number is less than 100")          
else:
    print("Number is negative")   

#19
print("Output for Question 19:.................................................")
age=int(input("Enter your age:")) 
if age>=18:
    if age<=60:
        print("Age Between 18 and 60")
    else:
        print("Age is greater than 60")        
else:
    print("Minor") 

#20
print("Output for Question 20:.................................................")
num=int(input("enter your Number:"))
if num!=0:
    if num>0:
        print("Number is Positive")
    else:
        print("Number is Negative")          
else:
    print("Number is Zero")   

#21
print("Output for Question 21:.................................................")
age=int(input("Enter your age:"))
marks=int(input("Enter your marks:"))      
if age>=18:
    if marks>=40:
        print("Eligible")
    else:
        print("Not Eligible")
else: 
    print("Not Eligible")                      

#22
print("Output for Question 22:.................................................")
num=int(input("Enter number:"))  
if num<10:
    print("number is special")
elif num>100:
    print("number is special")
else:
    print("number is betwwen 10 nad 100")

#23
print("Output for Question 23:.................................................")
age=int(input("Enter your age:"))
has_id=input("Enter id in True and False:").capitalize()
if age>=18:
    if has_id=="True":
        print("Allowed")
    else:
        print("id does not match")
else:
    print("Not Allowed")           

#24
print("Output for Question 24:.................................................")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>10:
    if num2>10:
        print("Both number is greater than 10")
    else:
        print("num1 is greater than 10 but num2 is less than 10")
elif num1<=10:
    if num2>10:
        print("num2 is greater than 10 but num1 is less than 10")
    elif num2<=10:
        print("both number are less than 10")

#25
print("Output for Question 25:.................................................")
num=int(input("Enter number:"))
if num<=0:
    if num==0:
        print("Number exect 0")
    else:
        print("Number is less than 0")    
elif num>=100:
    if num==100:
        print("Number exect 100")
    else:
        print("Number is greater than 100")            
else:
    print("Number is between 1 to 99")

#26
print("Output for Question 26:.................................................")
is_closed=False
if not is_closed:
    print("Open")

27 
print("Output for Question 27:.................................................") 
num=int(input("Enter number:"))
if num>=10 and num<=50:
    print("Number is between 10 and 50")
else:
    print("Other number")

#28  
print("Output for Question 28:.................................................") 
num=int(input("Enter number:"))
if num<=10 or num>=50:
    print("Number is Outside 10 and 50")
else:
    print("Number is between 10 and 50") 

29
print("Output for Question 29:.................................................")     
is_student=True
has_id=True
has_ticket=True
if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not allowed")    

#30
print("Output for Question 30:.................................................")
age=int(input("Enter your age:"))
marks=int(input("Enter your marks"))
has_id=True
if age>=18 and marks>=40 and has_id:
    print("Eligible")
else:
    print("Not eligible")    
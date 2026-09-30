#Level 1 – Basics (numbers, variables, if-else)
#1
num=int(input("Enter number :"))
if num%2==0:
    print("even")
else:
    print("odd")    

#2
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
if num1>num2:
    print(num1)
else:
    print(num2)    

#3
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))
if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)   
else:
    print(num3)     

#4
num=int(input("Enter number :"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#5
age=int(input("Enter age :"))
if age<=12:
    print("child")
elif age<=19:
    print("teenager")
else:
    print("adult")    

#6
marks=int(input("Enter your marks :"))
if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("F")       

#7
num=int(input("Enter number :"))
if num%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5") 

#8
num=int(input("Enter number :"))
if num%5==0 and num%3==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")

#9
year=int(input("Enter year :"))
if year%400==0 or year%4==0:
    print("leap year")
else:
    print("not a leap year")    

#10
num=int(input("Enter number :"))
if num>=10 and num<=50:
    print("in range")
else:
    print("out of range") 
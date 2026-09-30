#Level 1 — Intermediate
#1. Positive, Negative, or Zero
print("Output for Question 1:.................................................")
num=int(input("Enter number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative") 
else:
    print("Zero")   

#2. Even or Odd + Positive or Negative 
print("Output for Question 2:.................................................")
num=int(input("Enter number:"))
if num>0:
    if num%2==0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif num<0:
    if num%2==0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero") 

#3. Largest of Two Numbers
print("Output for Question 3:.................................................")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num1>num2:
    print("first number is larger")
elif num1<num2:
    print("second number is larger")   
else:
    print("Both are equal")  


#4. Smallest of Three Numbers
print("Output for Question 4:.................................................")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter thrid number:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print("num3 is smallest")
    else:
        print("num2 is smallest")
elif num2>num1 and num2>num3:
    if num1>num3:
        print("num3 is smallest")
    else:
        print("num1 is smallest")
elif num3>num2 and num3>num1:
    if num2>num1:
        print("num1 is smallest")
    else:
        print("num2 is smallest") 
else:
    print("Three are equal")                            

#5. Largest of Three Numbers
print("Output for Question 5:.................................................")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter thrid number:"))
if num1>num2 and num1>num3:
    print("num1 is largest")
elif num2>num1 and num2>num3:
    print("num2 is largest")
elif num3>num1 and num2<num3:
    print("num3 is largest")
else:
    print("Three are equal")

#6. Divisible by 5 and 11
print("Output for Question 6:.................................................")
num=int(input("Enter number:"))
if num%5==0 and num%11==0:
    print("Divisible by both 5 and 11")
elif num%5==0:
    print("Divisible only by 5") 
elif num%11==0:
    print("Divisible only by 11")       
else:
    print("Divisible by neither")

#7. Divisible by Either 3 or 7
print("Output for Question 7:.................................................")
num=int(input("Enter number:"))
if num%3==0 and num%7==0:
    print("Divisible by both 3 and 7")
elif num%3==0:
    print("Divisible only by 3") 
elif num%7==0:
    print("Divisible only by 7")       
else:
    print("Divisible by neither")

#8. Pass or Fail
print("Output for Question 8:.................................................")
marks=int(input("Enter your marks:"))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=40:
    print("Pass")
else:
    print("Fail")        

#9. Grade Calculator
print("Output for Question 9:.................................................")
marks=int(input("Enter your marks:"))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=90:
    print("A")
elif marks>=80:
    print("B") 
elif marks>=70:
    print("C") 
elif marks>=60:
    print("D")
elif marks>=40:
    print("E") 
else:
    print("Fail") 


#10. Voting Eligibility
print("Output for Question 10:.................................................")
age=int(input("Enter your age:"))
if age<0:
    print("Invalid age")
elif age<18:
    print("Cannot vote")
elif age<120:
    print("Can vote")   
else:
    print("Unrealistic age you can not vote")         

#Level 2 — More Logical Conditions
#11. Leap Year
print("Output for Question 11:.................................................")
year=int(input("Enter year:"))
if year%400==0 or year%4==0 and year%100!=0:
    print("Leap year")
else:
    print("Not a leap year")  

#12. Character Type
print("Output for Question 12:.................................................")
character=input("Enter char:")
if ord(character)>=65 and ord(character)<=91:
    print("Uppercase alphabet")
elif ord(character)>=97 and ord(character)<=123:
    print("Lowercase alphabet")
elif ord(character)>=48 and ord(character)<=57:
    print("Digit")
else:
    print("Special character")    

#13. Vowel or Consonant
print("Output for Question 13:.................................................")
character=input("Enter char:")
if ord(character)==97 or ord(character)==101 or ord(character)==105 or ord(character)==111 or ord(character)==117 or ord(character)==65 or ord(character)==69 or ord(character)==73 or ord(character)==79 or ord(character)==85:
    print("Vowel")
elif ord(character)>=48 and ord(character)<=57:
    print("Invalid input")     
elif ord(character)!=97 or ord(character)!=101 or ord(character)!=105 or ord(character)!=111 or ord(character)!=117 or ord(character)!=65 or ord(character)!=69 or ord(character)!=73 or ord(character)!=79 or ord(character)!=85 :
    print("Consonant") 


#14. Profit or Loss
print("Output for Question 14:.................................................")
cost_price=int(input("Enter cost price:"))
selling_price=int(input("Enter selling price:"))
if cost_price>selling_price:
    print("Loss =",cost_price-selling_price)
elif cost_price<selling_price:
    print("Profit =",selling_price-cost_price)    
else:
    print("No profit and no loss")    

#15. Profit/Loss Percentage
print("Output for Question 15:.................................................")
cost_price=int(input("Enter cost price:"))
selling_price=int(input("Enter selling price:"))
Profit = selling_price - cost_price
Loss = cost_price - selling_price
if cost_price<=0:
    print("Enter valid cost price")
elif Profit>0:
    print("Profit percentage:",Profit / cost_price * 100) 
elif Profit<0:
    print("Loss percentage:",Loss / cost_price * 100)      
else:
    print("No profit and no loss") 


#16. Electricity Bill
print("Output for Question 16:.................................................")
units=int(input("Enter electricity consumed units:"))
if units>200:
    bill=(units-200)*10+100*5+(100)*7
    print("your electricity bill is :",bill)
elif units>100:
    bill=(units-100)*7+100*5
    print("your electricity bill is :",bill)
elif units>0:
    bill=units*5
    print("your electricity bill is :",bill)
else:
    print("enter valid value of units")

#17. Simple Calculator
print("Output for Question 17:.................................................")
num1=float(input("first number:"))
num2=float(input("second number:"))
Your_Choice=input("Operations would you like : \n addition=+ \n subtraction=- \n mulitiply=* \n division=/ \n ")
if Your_Choice=="+":
    print(num1+num2)
elif Your_Choice=="-":
    print(num1-num2)
elif Your_Choice=="*":
    print(num1*num2)
elif Your_Choice=="/":
    if num2!=0:
        print(num1/num2) 
    else:
        print("second number not be zero")    
else:
    print("your choice is out of range")

#18. Temperature Classifier
print("Output for Question 18:.................................................")
temp=int(input("Enter temperature in Celsius:"))
if temp>35:
    print("Hot")
elif temp>25:
    print("Normal")
elif temp>15:
    print("Cold")    
elif temp>=0:
    print("Very Cold") 
else:
    print("Freezing")          


#19. Number Range Checker
print("Output for Question 19:.................................................")
num=int(input("Enter number:"))
if num>100:
    print("Number is Above 100")
elif num>50:
    print("Number is between 51 and 100")
elif num>10:
    print("Number is between 11 and 50")  
elif num>=0:
    print("Number is between 0 and 10")    
else:
    print("Number is Negative")      

#20. Triangle Validator
print("Output for Question 20:.................................................")
a,b,c=map(int,input("Enter three sides of triangle:").split(","))
if a+b>c and b+c>a and a+c>b:
    print("Valid triangle")
else:
    print("Invalid triangle")

#Level 3 — Harder Conditional Problems
#21. Triangle Type
print("Output for Question 21:.................................................")
a,b,c=map(int,input("Enter three sides of triangle by , sepatreted:").split(","))
if a+b>c and b+c>a and a+c>b:
    print("Valid triangle")
    if a==b==c:
        print("Equilateral → all three sides equal")
    elif a==b or b==c or c==a:
        print("Isosceles   → exactly two sides equal")    
    else:
        print("Scalene     → all sides different")    
else:
    print("Invalid triangle")     

#22. ATM Withdrawal 
print("Output for Question 22:.................................................")
Account_balance=int(input("Enter Account balance:"))
Withdrawal_amount=int(input("Enter Withdrawal amount:"))
if Withdrawal_amount>0 and Withdrawal_amount%100==0 and Withdrawal_amount+500<Account_balance:
    print("Withdrawal successful", "\n Remaining balance :",Account_balance-Withdrawal_amount)
elif Withdrawal_amount<=0:
    print("withdraval amount cannot be zero")
elif Withdrawal_amount%100!=0:
    print("withdrawal amount divisle by 100")
else:
    print("After withdrawal, at least ₹500 must remain")    

#23. Login System
print("Output for Question 23:.................................................")
Username=input("Enter username :")
Password=input("Enter password :")
if Username=="admin" and Password=="python123":
    print("Login successful")
elif Username!="admin" and Password=="python123":
    print("User not found")
elif Username=="admin" and Password!="python123":
    print("Wrong password")
else:
    print("both not found")    

#24. Discount Calculator
print("Output for Question 24:.................................................")
purchase_amount=int(input("Enter purchase amount:"))
if purchase_amount>=5000:
    Discount_amount=purchase_amount*20/100
    print("Discount: 20%","\n Discount amount:" ,Discount_amount,"\n Final amount:" ,purchase_amount-Discount_amount)
elif purchase_amount>=2000:
    Discount_amount=purchase_amount*15/100
    print("Discount: 15%","\n Discount amount:" ,Discount_amount,"\n Final amount:" ,purchase_amount-Discount_amount)
elif purchase_amount>=1000:
    Discount_amount=purchase_amount*10/100
    print("Discount: 10%","\n Discount amount:" ,Discount_amount,"\n Final amount:" ,purchase_amount-Discount_amount) 
elif purchase_amount>=500:
    Discount_amount=purchase_amount*5/100
    print("Discount: 5%","\n Discount amount:" ,Discount_amount,"\n Final amount:" ,purchase_amount-Discount_amount)  
elif purchase_amount>0:
    Discount_amount=purchase_amount*0/100
    print("Discount: 0%","\n Discount amount:" ,Discount_amount,"\n Final amount:" ,purchase_amount-Discount_amount) 
else:
    print("purchase amount cannot be negative or zero")   

#25. Student Result System
print("Output for Question 25:.................................................")
marks1=int(input("marks of subject1:"))          
marks2=int(input("marks of subject2:"))          
marks3=int(input("marks of subject3:")) 
if 0<=marks1<=100 and 0<=marks2<=100 and 0<=marks3<=100: 
    if marks1<35 or marks2<35 or marks3<35:
        print("Fail")    
    else:
        total_marks=marks1+marks2+marks3    
        avg_marks=total_marks/3
        if avg_marks>=75:
            print("Distinction")
        elif avg_marks>=60:
            print("First Class") 
        elif avg_marks>=50:
            print("Second Class")   
        else:
            print("Pass") 
else:
    print("give marks in range 0 to 100")

#26. Date Validator
print("Output for Question 26:.................................................")
Day=int(input("Enter day:"))                 
Month=int(input("Enter month:"))                 
Year=int(input("Enter year:"))  
if 0<Day<32 and 0<Month<13 and Year>0:
    if Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12:
        print("valid")
    elif(Month==4 or Month==6 or Month==9 or Month==11) and Day<31:
        print("valid")
    elif (Month==4 or Month==6 or Month==9 or Month==11) and Day==31:  
        print("date is not valid")  
    else:
        if Month==2 and (Year%400==0 or Year%4==0) and Year%100!=0 and Day==29:  
            print("valid")  
        elif Month==2 and Day<29:
            print("valid")
        else:
            print("date is not valid")    
else:
    print("date is not valid")                   

#27. Time Validator
print("Output for Question 27:.................................................")
Hours=int(input("Enter hour:"))
Minutes=int(input("Enter minute:"))
Seconds=int(input("Enter second:"))
if 0<=Hours<=23 and 0<=Minutes<=59 and 0<=Seconds<=59:
    print("Valid time")
else:
    print("Not Valid time") 

#28. Youngest of Three People
print("Output for Question 28:.................................................")
name_person1=input("Enter your name:")
age_person1=int(input("Enter your age:"))
name_person2=input("Enter your name:")
age_person2=int(input("Enter your age:"))
name_person3=input("Enter your name:")
age_person3=int(input("Enter your age:"))
if age_person1<age_person2 and age_person1<age_person3:
    print(f"{name_person1} is the youngest")
elif age_person2<age_person1 and age_person2<age_person3:
    print(f"{name_person2} is the youngest")
elif age_person3<age_person2 and age_person3<age_person1:
    print(f"{name_person3} is the youngest")  
elif age_person1==age_person2==age_person3:
    print("all are same age")
else:
    if age_person1==age_person2!=age_person3:
        print(f"{name_person1} and {name_person2} are same age")
    elif age_person3==age_person2!=age_person1:
        print(f"{name_person3} and {name_person2} are same age")
    else:
        print(f"{name_person1} and {name_person3} are same age")      

#29. Second Largest of Three Numbers
print("Output for Question 29:.................................................")
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"Middle number is {num2}")
    else:
        print(f"Middle number is {num3}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"Middle number is {num1}")  
    else:
        print(f"Middle number is {num3}") 
elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"Middle number is {num1}")
    else:
        print(f"Middle number is {num2}")                     
elif num1==num2==num3:
    print(f"Middle number is {num2}")
else:
    if num1==num2:
        print(f"Middle number is {num2}")
    elif num1==num3:
        print(f"Middle number is {num1}")
    else:
        print(f"Middle number is {num2}") 


#30. Complete Scholarship Decision
print("Output for Question 30:.................................................")
student_age=int(input("Enter student age:"))
marks=int(input("Enter student marks:"))
family_income=int(input("Enter family income:"))
attendance_percentage=int(input("Enter student attendance percentage:"))
if 18<=student_age<=25 and 85<=marks<=100 and 0<=family_income<=30000 and  75<=attendance_percentage<=100:
    print("Scholarship Approved")
elif not 18<=student_age<=25:
    print("Scholarship Rejected \nReason: Student age is not satisfied")
elif not 85<=marks<=100:
    print("Scholarship Rejected \nReason: Marks below 85")
elif not 0<=family_income<=30000:
    print("Scholarship Rejected \nReason: family income more than 30000") 
elif not 75<=attendance_percentage<=100:
    print("Scholarship Rejected \nReason: attendance is less than 75%")      
else:
    print("Enter valid values")
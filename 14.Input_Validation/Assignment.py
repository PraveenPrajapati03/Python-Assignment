#Part A — Intermediate Problems
#1
while True:
    marks=int(input("Enter marks :"))
    if marks<0 or marks>100:
        print("invalid marks")
    else:
        print("accepted marks")
        break

#2
while True:
    num=int(input("Enter number :"))
    if num<=0:
        print("invalid number")
    else:
        print("accepted number")
        break

#3
while True:
    age=int(input("Enter your age :"))
    if age<0 or age>120:
        print("invalid age")
    else:
        print("accepted age")
        break

#4
while True:
    choice=int(input("Enter \n1. View profile\n2. Edit profile\n3. Settings\n\n4. Exit :\n===>"))
    if choice<=0 or choice>4:
        print("invalid choice")
    else:
        print(f"accepted option {choice}")
        break

#5
while True:
    password=input("Enter password (minimum 8 letter):").strip()
    if len(password)<8:
        print("invalid password")
    else:
        print("accepted password")
        break

#6
while True:
    temp=int(input("Enter temperature between -20 to 45 :"))
    if temp<-20 or temp>45:
        print("invalid tempearture")
    else:
        print("accepted tempearture")
        break

#7
balance=5000
while True:
    withdrawal_amount=int(input("Enter withdrawal amount :"))
    if withdrawal_amount<=0 or withdrawal_amount>5000:
        print("invalid amount")
    else:
        print("balance :",balance-withdrawal_amount)
        break

8
while True:
    username = input("Enter your username: ").strip()
    if len(username) >= 5 and " " not in username:
        break
    print("Invalid username")
print("Accepted username:", username)

#9
while True:
    num=int(input("Enter number is divide by 3 and 5 :"))
    if num<0 or num%3!=0 or num%5!=0:
        print("invalid number")
    else:
        print("accepted number")
        break

#10
for i in range(3):
    pin=int(input("Enter secret pin:"))
    secret_PIN=2468
    if pin==secret_PIN:
        print("PIN is correct")
        break
else:
    print("access is denied")

#11
while True:
    num=int(input("Enter number between 10 to 50 :"))
    if num<10 or num>50:
        print("invalid number")
    else:
        if num%2==0:
            print("number is even")
        else:
            print("number is odd")
        print("accepted number")
        break

#12
balance=2000
while True:
    deposit_amount=int(input("Enter deposit amount :"))
    if deposit_amount<=0:
        print("invalid deposit amount")
    else:
        print("new balance :",balance+deposit_amount)
        break

#Part B — Challenging Problems
#13
while True:
    num=int(input("Enter number between 1 to 100 :"))
    if num<=0 or num>100:
        print("invalid number")
    else:
        print("accepted number")
        break

#14
while True:
    marks=int(input("Enter marks :"))
    if marks<0 or marks>100:
        print("invalid marks")
    else:
        if marks>=75:
            print("Distinction")
        elif marks>=60:
            print("First Class")
        elif marks>=35:
            print("Pass")
        else:
            print("Fail")
        print("accepted marks")
        break

#15
while True:
    username = input("Enter your username:").strip()
    password=input("Enter password (minimum 8 letter):").strip()
    if len(username)<5 or " " in username or len(password)<8 or " " in password:
        print("Invalid")
    else:
        print("accepted")
        break

#16
while True:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    operator = input("Enter operator (+, -, *, /):")
    while operator not in "+-*/" or len(operator)!=1:
        print("Invalid operator")
        operator=input("Enter operator (+, -, *, /) :")
    else:
        if operator == "+":
            print("Result :",num1+num2)
        elif operator == "-":
            print("Result :",num1-num2)
        elif operator == "*":
            print("Result :",num1*num2)
        else:
            while num2==0:
                print("Second number must not be zero")
                num2 = int(input("Enter second number again:"))
            else:
                print("Result :",num1/num2)
        break

#17
balance = 10000
while True:
    option = int(input("Select a option \n 1. Check balance \n 2. Deposit money \n 3. Withdraw money \n 4. Exit \n ====>: "))
    while option < 1 or option > 4:
        print("invalid option choice")
        option = int(input("Select a option \n 1. Check balance \n 2. Deposit money \n 3. Withdraw money \n 4. Exit \n ====>: "))
    else:
        if option == 1:
            print(balance)
        elif option == 2:
            deposit_amount=int(input("Enter the amount to deposit: "))
            while deposit_amount < 0:
                print("deposit amount not less then 0")
                deposit_amount=int(input("Enter the amount to deposit: "))
            else:
                balance += deposit_amount
                print(balance)
        elif option == 3:
            withdrawl_amount = int(input("Enter the amount to withdrawl: "))
            while withdrawl_amount < 0 or withdrawl_amount > balance:
                print("invalid withdrawal amount")
                withdrawl_amount = int(input("Enter the amount to withdrawl: "))
            else:
                print(balance)
                balance -= withdrawl_amount
        else:
            break

#18
while True:
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    while month < 1 or month > 12 or day > 31 or day < 1:
        print("invalid values")
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
    else:
        print("Day and Month Accepted")
        break

#19
while True:
    product_quantity = int(input("Enter product quantity: "))
    while product_quantity <= 0:
        print("Product quantity must be a positive integer.")
        product_quantity = int(input("Enter product quantity: "))
    unit_price = float(input("Enter one item price: "))
    while unit_price <= 0:
        print("Unit price must be greater than zero.")
        unit_price = float(input("Enter one item price again: "))
    print("Total cost:", product_quantity * unit_price)
    break

#20
while True:
    count=int(input("Enter how many numbers they want to enter :"))
    while count<=0 or count>20:
        print("invalid choice")
        count=int(input("Enter how many numbers they want to enter agian :"))
    total=0
    for i in range(count):
        number=int(input("Enter number :"))
        total+=number
    avg=total/count
    print("average of all numbers is :",avg)
    break

#21
while True:
    condition_satisfied = 0
    password = input("Enter password: ").strip()
    print()
    if len(password) >= 8:
        condition_satisfied += 1
    else:
        print("Password need atleast 8 characters.")
    for character in password:
        if character == " ":
            print("Password should not have whitespace characters.")
            break
    else:
        condition_satisfied += 1
    for character in password:
        if 65 <= ord(character) <= 90:
            condition_satisfied += 1
            break
    else:
        print("There should be atleast one uppercase letter.")
    for character in password:
        if 97 <= ord(character) <= 122:
            condition_satisfied += 1
            break
    else:
        print("There should be atleast one lowercase letter.")
    for character in password:
        if 48 <= ord(character) <= 57:
            condition_satisfied += 1
            break
    else:
        print("There should be atleast one digit.")
    if condition_satisfied == 5:
        break
print("Password Accepted")

#22
while True:
    number = int(input("Enter a number :"))
    while number < 0 or number > 10:
        print("invalid number")
        number = int(input("Enter a number agian :"))
    else:
        print("Number Accepted")

#23
score_1 = int(input("Enter score 1: "))
score_2 = int(input("Enter score 2: "))
score_3 = int(input("Enter score 3: "))
while score_1 < 0 or score_1 > 100:
    score_1 = int(input("Enter score 1: "))
while score_2 < 0 or score_2 > 100:
    score_2 = int(input("Enter score 2: "))
while score_3 < 0 or score_3 > 100:
    score_3 = int(input("Enter score 3: "))
print("Total:", score_1 + score_2 + score_3)
print("Average:", (score_1 + score_2 + score_3) / 3)

#24
balance = 10000
while True:
    withdrawl_amount = int(input("Enter the amount to withdraw: "))
    if withdrawl_amount < 0:
        continue
    elif withdrawl_amount > balance:
        continue
    elif withdrawl_amount % 100 != 0:
        continue
    else:
        break
balance -= withdrawl_amount
print(f"The withdrawl amount is Rs.{withdrawl_amount}")
print(f"The remaining balance is Rs.{balance}")
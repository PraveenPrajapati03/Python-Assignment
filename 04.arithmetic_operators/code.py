#Part 3 — Practical Programs
#Task 1 — Basic Arithmetic
num1=10
num2=3
print("Output for task 1:")
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

#Task 2 — Integer and Float
num1=10
num2=5.5
print("Output for task 2:")
print(num1+num2,type(num1+num2))
print(num1-num2,type(num1-num2))
print(num1*num2,type(num1*num2))
print(num1/num2,type(num1/num2))
print(num1//num2,type(num1//num2))
print(num1%num2,type(num1%num2))
print(num1**num2,type(num1**num2))

#Task 3 — Student Marks
html=95
css=96
python=100
total_marks=html+css+python
avg_marks=total_marks/3
print("Output for task 3:")
print("total_mark:",total_marks)
print("avg_mark:",avg_marks)

#Task 4 — Product Calculation
price=2000
quantity=10
total_price=price*quantity
print("Output for task 4:")
print("total_price:",total_price)

#Task 5 — Even or Odd
number = 10
print("Output for task 5:")
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Task 6 — Division and Floor Division
num1=10
num2=3
num3=-10
print("Output for task 6:")
print(num1/num2)
print(num1//num2)
print(num3/num2)
print(num3//num2)

#Task 7 — Negative Number Operations
num1=-10
num2=-3
print("Output for task 7:")
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1%num2)
print(num1**num2)

#Task 8 — Subtraction Edge Cases
num1=10
num2=5
num3=-10
num4=-5
print("Output for task 8:")
print(num1-num2)
print(num1-num4)
print(num3-num2)
print(num3-num4)

#Task 9 — Floor Division Edge Cases
num1=10
num2=3
num3=-10
num4=-3
print("Output for task 9:")
print(num1//num2)
print(num1//num4)
print(num3//num2)
print(num3//num4)

#Task 10 — Modulus Edge Cases
num1=10
num2=3
num3=-10
num4=-3
print("Output for task 10:")
print(num1%num2)
print(num1%num4)
print(num3%num2)
print(num3%num4)

#Part 4 — Operator Precedence
#Task 11
print("Output for task 11:")
print(10 + 5 * 2)
print(20 - 4 / 2)
print(10 + 20 / 5 * 2)
print(2 + 3 * 4 ** 2)
print(100 - 20 // 5)

#Task 12 — Parentheses
print("Output for task 12:")
print(10 + 5 * 2 , (10 + 5)* 2)
print(20 - 10 / 2,(20 - 10) / 2)
print(2 + 3 * 4,(2 + 3) * 4)

#Part 5 — Boolean Arithmetic
#Task 13
num1=True
num2=False
print("Output for task 13:")
print(num1+num2,type(num1+num2))
print(num1-num2,type(num1-num2))
print(num1*num2,type(num1*num2))
print(num2/num1,type(num2/num1))
print(num2//num1,type(num2//num1))
print(num2%num1,type(num2%num1))
print(num1**num2,type(num1**num2))

#Task 14
print("Output for task 14:",True + 5,
False + 5,
True * 10,
False * 10,
True - 5,
False - 5)

#Part 6 — String Operations
#Task 15
first_name="Praveen"
last_name="Prajapati"
print("Output for task 15:",first_name+ " " +last_name)

#Task 16
first_name="Praveen"
last_name="Prajapati"
print("Output for task 16:",(first_name+ " " +last_name)*3)

#Task 17
first_name="Praveen"
last_name="Prajapati"
print("Output for task 17:",first_name+ " " +last_name,(first_name+ " " +last_name)*3)
print("The Subtraction and Division show the Type error ........")

#Part 7 — None Type
#Task 18
value=None
num1=10
print("Output for task 18:","Python show- TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' ")

#Part 8 — Error Handling Practice
#Task 19
num1=1
num2=0
print("Output for task 19:","Python shows - ZeroDivisionError: division by zero")

#Part 9 — Combined Challenge
#Task 20 — Mini Calculator
num1=10
num2=3
print("Output for task 20:")
print("Addition:",num1+num2)
print("Subtraction:",num1-num2)
print("Multiplication:",num1*num2)
print("Division:", num1/num2)
print("Floor Division:",num1//num2)
print("Modulus:",num1%num2)
print("Exponentiation:",num1**num2)

#Part 10 — Final Challenge
#Task 21 — Arithmetic Expression Analyzer
a = 10
b = -3
c = 2.5
print("Output for task 21:")
print(a + b)
print(a - b)
print(a * c)
print(a / c)
print(a // b)
print(a % b)
print(a ** 2)
print((a + b) * c)
print(a + b * c)
print((a - b) / c)
print(a ** 2 + b * c)
print((a + c) // 2)

# Q1
add = lambda num1,num2:num1+num2
print(add(10,20))

# Q2
square = lambda n:n*n
print(square(6))

# Q3
cube = lambda n:n**3
print(cube(3))

# Q4
check = lambda n:"Even" if n%2==0 else "Odd"
print(check(7))

# Q5
greater = lambda a,b:a if a>b else b
print(greater(45,32))

# Q6
Fahrenheit = lambda c:(c)*9/5+32
print(Fahrenheit(25))

# Q7
length = lambda str:len(str)
print(length("python"))

# Q8
upper = lambda str:str.upper()
print(upper("hello world"))

# Q9
last_ch = lambda str:str[-1]
print(last_ch("Coding"))

# Q10
final_price = lambda price,discount:price-price*discount/100
print(final_price(1000,10))
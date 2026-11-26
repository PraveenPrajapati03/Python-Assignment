# Q1
def func():
    city="nagaur"
    print(city)
func()

# Q2
school="JNV Jalore"
def display():
    print(school)
display()

# Q3
if True:
    name = "Praveen"
print(name)

# Q4
i = 0
for i in range(1, 6):
    print(i)
print("After loop:", i)

# Q5
# Scope = Where a variable can be accessed.
# Lifetime = How long a variable exists.

# Q6
value = 100
def test():
    value = 200
    print(value)
test() #200
print(value) #100

# Q7
clicks = 0
def click():
    global clicks
    clicks += 1

# Q8
name = "Asha"
def show():
    name = "Ravi"
    print(name)
show()
# This code raises an UnboundLocalError because Python treats name as a local variable inside the show() function due to the assignment name = "Ravi"

# Q9
def outer():
    name = "praveen"
    def inner():
        print(name)
    inner()
outer()

# Q10
def get_numbers():
    return [10, 20, 30, 40]
numbers = get_numbers()
print("Original list:", numbers)
numbers.append(50)
numbers[0] = 100
print("Modified list:", numbers)

# Q11
def outer():
    count=0
    def inner():
        nonlocal count
        count+=1
        return count
    return inner
count=outer()
print(count())
print(count())
print(count())

# Q12
x=1
def outer():
    x=2
    def inner():
        x=3
        print(x)
    inner()
    print(x)
outer()
print(x)

# Q13
#In Python, normal for loops do not create a separate scope, but list comprehensions create their own scope in Python 3

# Q14
def outter():
    count=0
    def inner():
        nonlocal count
        count+=1
        return count
    return inner
count=outter()
print(count())
print(count())
print(count())

# Q15
# because they are the inbuilt function and if the any variable is not found then the it search for the inbulid so be avoid to use the inbuild function anme for the variable name
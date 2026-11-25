# Q1
def show(n):
    if n == 0:
        print("Stop")
        return
    print(n)
    show(n - 1)
    print(n)
show(2)

# def show(2):
#     if 2 == 0:
#         print("Stop")
#         return
#     print(2)
#     show(2 - 1)
#     print(2)

# def show(1):
#     if 1 == 0:
#         print("Stop")
#         return
#     print(1)
#     show(1 - 1)
#     print(1)

# def show(0):
#     if 0 == 0:
#         print("Stop")
#         return


# Q2
def total(n):
    if n == 0:           #base case
        return 0

    return n + total(n - 1)
# if n > 0 => the recursion stop because the value of n decrease by 1 each time a function run, and value of n become equal to base case value.
# if n < 0 => the recrusion stop because the function run for infinite time which cause it to raise recrussion error.


# Q3
def count(n):
    if n == 0:
        return
    count(n + 1)
# This function does not reach its base case when called with count(2), because value of n increase by 1 for every function call 
# but value of n is aleardy greater than base case value and it can't reach base case so it will cause recrusion error


# Q4
def answer(n):
    if n == 0:
        return 0
    n + answer(n - 1)
print(answer(3))
# It will result in an error as n is of int datatype whereas answer(n - 1) is of NoneType datatype.


# Q5
def countdown(n):
    if n == 0:
        return "Done!"
    print(n)
    return countdown(n - 1)
print(countdown(3))


# Q6
def count_up(n):
    if n == 0:
        return
    count_up(n - 1)
    print(n)
count_up(4)


# Q7
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n-1)
print(sum_to(5))
print(sum_to(0))


# Q8
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(4))
print(factorial(0))


# Q9
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)
print(digit_sum(583))
print(digit_sum(7))
print(digit_sum(0))


# Q10
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base,exponent-1)
print(power(2, 5))  
print(power(9, 0))  
print(power(3, 1))  


# Q11
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
print(count_digits(5382))  
print(count_digits(6))     
print(count_digits(0))  


# Q12
def reverse_text(text):
    if text == "":
        return ""
    return text[-1] + reverse_text(text[:len(text)-1])
print(reverse_text("cat"))  
print(reverse_text("a"))   
print(reverse_text(""))


# Q13
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(6))


# Q14
def max_digit(n):
    if n == 0:
        return 0
    last_digit = n % 10
    remaining_max = max_digit(n // 10)
    if last_digit > remaining_max:
        return last_digit
    else:
        return remaining_max
print(max_digit(4729))


# Q15
def mystery(n):
    if n <= 1:
        return n
    return mystery(n - 1) + mystery(n - 2)
print(mystery(4)) #3
print(mystery(0)) #0
print(mystery(1)) #1
print(mystery(2)) #1


# Q16
def factorial(n):
    if n == 0:
        return 1  #0=>1
    return n * factorial(n - 1)


# Q17
def stop_at_zero(n):
    if n == 0:
        return
    stop_at_zero(n - 1)  #n=>n-1


# Q18
# If a recursive function makes too many nested calls, it exceeds the recursion limit which cause in the 'RecusrionError'.
# A loop is a better choice for a very large counting task as it dosen't have any limit and it will not cause any limit errors, unlike recursion which has a limit and cause error if the limit exceeds
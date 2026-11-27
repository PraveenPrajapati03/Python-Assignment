# Q1
result=0
count=1
def even_sum(n):
    global count,result
    last_digit=n%10
    if count%2==0:
        result+=last_digit
    else:
        result+=0    
    count+=1
    if n<10:
        return n   
    even_sum(n//10)
    return result
print(even_sum(583246))


# Q2
result=0
def reverse(n):
    global result
    last_digit=n%10
    result=result*10+last_digit
    if n<10:
        return n
    reverse(n//10)
    return result
print(reverse(4827))


# Q3
def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome(s,left+1,right-1)
print(palindrome("level",0,len("level")-1))


# Q4
count=0
p=0
def counter(str,ch):
    global count,p
    if len(str)<=p:
        return True
    if str[p]==ch:
        count+=1
    p+=1
    counter(str,ch)
    return count
print(counter("programming", "m"))


# Q5
gn=0
count = 0
def gcd(num1,num2):
    global gn, count,min
    if min== count:
        return gn
    if num1>num2:
        min=num2
    else:
        min=num1
    count+=1
    if num1%count==0 and num2%count==0:
        gn=count
    gcd(num1,num2)
    return gn
print(gcd(6,48))


# Q6
def prime(n, count=2):
    if count >= n:
        return True
    if n % count == 0:
        return False
    return prime(n, count + 1)
print(prime(29))
print(prime(28))


# Q7
result = ""
def remover(string, char):
    global result
    if string == "":
        return
    remover(string[:-1], char)
    if string[-1] == char:
        return
    result += string[-1]
    return result
print(remover("mississippi", "s"))


# Q8
result = 0
bn = 0
def binary(n):
    global result, bn
    if n <= 1:
        result = n + result * 10
        return result
    bn = n % 2
    result = result * 10 + bn
    binary(n // 2)
    return result
print(binary(13))


# Q9
def digit_checker(n):
    if n<10:
        return
    digit_checker(n// 10)
    if 0 <= n % 10 <= 9:
        return True
print(digit_checker(50291))


# Q10
def digital_root(n):
    if n < 10:
        return n
    return digital_root(n % 10 + digital_root(n // 10))
print(digital_root(9875))
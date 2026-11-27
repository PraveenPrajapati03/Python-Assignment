# Q1
message="Hello"
def displayhello(message, n = 3):
    if n == 0:
        return 0
    print(message)
    return displayhello(message,n-1)
displayhello(message,3)

# Q2
def evennumber(n):
    if n==0:
        return 0
    if n%2==0:
        print(n)
    return evennumber(n-1)
evennumber(10)

# Q3
result=0
def oddsum(n):
    global result
    if n==0:
        return 0
    if n%2!=0:
        result+=n
    oddsum(n-1)
    return result
print(oddsum(7))

# Q4
count=0
def counter(n,target):
    global count
    last_digit=n%10
    if last_digit==target:
        count+=1
    if n<10:
        return n
    counter(n//10,target)
    return count
print(counter(52525,5))

# Q5
product=1
def mul(n):
    global product
    last_digit=n%10
    product*=last_digit
    if n<10:
        return n
    mul(n//10)
    return product
print(mul(234))

# Q6
def firstdigit(n):
    if n<10:
        return n
    return firstdigit(n//10)
print(firstdigit(5837))

# Q7
flag=False
def counter(n,target):
    global flag
    last_digit=n%10
    if last_digit==target:
        flag=True
    if n<10:
        return n
    counter(n//10,target)
    return flag
print(counter(4826,8))

# Q8
def length(str,count):
    if str=="":
        return count
    return length(str[:-1],count+1)
print(length("praveen",0))

# Q9
count=0
def vowel(str):
    global count
    if str=="":
        return ""
    if str[-1] in "aeiou":
        count+=1
    vowel(str[:-1])
    return count
print(vowel("education"))

# Q10
def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome(s,left+1,right-1)
print(palindrome("level",0,len("level")-1))                             
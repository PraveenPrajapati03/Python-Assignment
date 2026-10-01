#Level 5 – More string practice
#41
string=input("Enter string :").split()
print(len(string))\

#42
string=input("Enter string :")
string=string.replace("a","e")
print(string)

#43
string=input("Enter string :")
ch=input("Enter character to check in string :")
print(ch in string)

#44
string1=input("Enter first string :")
string2=input("Enter second string :")
print(string1==string2)

#45
string=input("Enter string :")
count=0
for i in string:
    if i.isdigit():
        count+=1
print(count)

#46
string=input("Enter string :")
count=0
for i in string:
    if i.isupper():
        count+=1
print(count)

#47
string=input("Enter string :")
count=0
for i in string:
    if i.islower():
        count+=1
print(count)

#48
string=input("Enter string :")
word=""
for i in string:
    if i in "AEIOUaeiou":
        word+=""
    else:
        word+=i
print(word)

#49
string=input("Enter string :")
word=""
for i in string:
    if chr(48)<=i<=chr(57):
        word+=""
    else:
        word+=i
print(word)

#50
string=input("Enter string :")
print(string.swapcase())
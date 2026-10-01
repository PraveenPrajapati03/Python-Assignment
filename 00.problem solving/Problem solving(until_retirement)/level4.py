#Level 4 – Strings
#31
string=input("Enter string :")
print(len(string))

#32
string=input("Enter string :")
for i in string:
    print(i)

#33
string=input("Enter string :")
count=0
for i in string:
    if i in "AEIOUaeiou":
        count+=1
print(count)

#34
string=input("Enter string :")
count=0
for i in string:
    if i not in "AEIOUaeiou":
        count+=1
print(count)

#35
string=input("Enter string :")
print(string.upper())

#36
string=input("Enter string :")
print(string.lower())

#37
string=input("Enter string :")
print(string[::-1])

#38
string=input("Enter string :")
rstring=string[::-1]
if string==rstring:
    print("true")
else:
    print("false")

#39
string=input("Enter string :").lower()
a=string.count("a")
print(a)

#40
string=input("Enter string :")
string=string.replace(" ","")
print(string)
#Section A --- Practice Problems on break
#1
for i in range(1, 8):
    if i == 5:
        break
    print(i)
print("Finished")
#Output==>1 2 3 4 Finished

#2
word = "skyline"
for ch in word:
    if ch in "aeiou":
        break
    print(ch)
#Output==>s k y l

#3
n = 2
while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2
#Output==>2 4 6 

#4
limit=int(input("Enter number limit :"))
for i in range(1,limit+1):
    if i==7:
        break
    print(i,end=" ")


#5
string=input("Enter string :")
target_character=input("Enter target character :")
for ch in string:
    print(ch,end=" ")
    if ch==target_character:
        break

#6
sequence=[4,8,2,-3,9]
for number in sequence:
    if number<0:
        break
    print(number)

#7
for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)
#Output==>1 1  1 2  2 1  2 2  3 1  3 2

#8
string=input("Enter string :").split()
target_word=input("Enter target character :")
for ch in string:
    if ch==target_word:
        print("Found")
        break

# Section B --- Practice Problems on continue
#9
for i in range(1, 7):
    if i == 4:
        continue
    print(i)
#Output==>1 2 3 5 6

#10
for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
#Output==>dctn

#11
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
#Output==>1 2 4 5

#12
n=int(input("Enter number :"))
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i)

#13
string=input("Enter string :")
character=input("Enter character :")
for i in string:
    if i==character:
        continue
    print(i,end="")

#14
numbers=""
for i in range(5):
    num=int(input("Enter number :"))
    numbers+=str(num)+" "
for number in numbers.split():
    if int(number)<40:
        continue
    print(number,end=" ")

#15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)
#Output==>A 1  B 1  A 3  B 3  A 4  B 4

#16
n = 0
while n < 5:
    if n == 3:
        n+=1
        continue
    n += 1
    print(n)

#17
word=input("Enter string :")
count=0
for ch in word:
    if ch in "aeiou":
        continue
    count+=1
print(count)

#Section C --- Practice Problems on for-else
#18
for i in range(1, 4):
    print(i)
else:
    print("Done")
#Output==>1 2 3 Done

#19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")
#Output==>1 3 4 Completed

#20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")
#Output==>1 2 Outside loop

#21
for item in []:
    print("Inside")
else:
    print("Else block")
#Output==>Else block

#22
numbers=[4,8,12,16]
target_number=int(input("Enter check number in list :"))
for number in numbers:
    if number==target_number:
        print("Found")
        break
else:
    print("Not found")

#23
string=input("Enter string :")
target_character=input("Enter target character :")
for ch in string:
    if ch==target_character:
        print("Character exists")
        break
else:
    print("Character missing")

#24
num=int(input("Enter number :"))
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        break
else:
    print("prime number")

#25
values = [2, 4, 6, 8]
for value in values:
    if value % 2 != 0:
        print("Odd found")
        break
else:
    print("All are even")
#Output==>All are even

#26
#Case A
for x in range(3):
    continue
else:
    print("A")
#Output==>A
#Case B
for x in range(3):
    break
else:
    print("B")
#Output==>Nothing
#Case C
for x in range(0):
    print(x)
else:
    print("C")
#Output==>C

#27
string = input("Enter sentence:")
a=0
for i in string:
    count = 0
    for j in string:
        if i==j:
            count += 1
    if count>=2:
        print(i)
        break
else:
    print("No repeated character")

#28
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
#Output==>1 2 3

#29
x = 10
if x > 5:
    pass
print("Finished")
#Output==>Finished

#30
for letter in "cat":
    pass
print("Loop ended")
#Output==>Loop ended

#31
for i in range(1,6):
    if i%2==0:
        pass
    print(i)

#32
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Option 1 selected")
elif choice == 2:
    pass
else:
    print("Unknown option")
print("Program closed")

#33
#Program A
for i in range(1, 5):
    if i == 3:
        pass
    print(i)
#Output==>1 2 3 4
#Program B
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
#Output==>1 2 4

#34
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#35
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")
#Output==>1 3

#36
numbers=[1,-2,3,-4,5,-6,7,8]
target_number=int(input("Enter target number :"))
for number in numbers:
    if number<0:
        continue
    elif number==target_number:
        print("Target found")
        break
else:
    print("Target not found")    

#37
numbers=[1,0,4,-5,2,-7,0]
for number in numbers:
    if number==0:
        continue
    elif number<0:
        break
    else:
        print(number,end=" ")
else:
    print("All values processed")

#38
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")
#Output1==>1 1  1 3  2 1  2 3
#Output2==>for row=1 and 2 inner loops finish without break
#Output3==>not for row 3 does not run

#39
numbers=[-3,8,12,24]
for number in numbers:
    if number<0:
        continue
    elif number%4==0 and number%6==0:
        print("Found:",number)
        break
else:
    print("No matching number")

#40
#1
while True:
    username=input("Enter username :")
    if username=="praveen_limba":
        break

#2
string=input("enter string :")
for i in string:
    if i==" ":
        continue
    print(i,end="")

#3
numbers = [10, 20, 30, 40]
target = int(input("Enter number:"))
for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not found")

#4
def sum():
    pass

#5
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

#6
while True:
    value = input("Enter a number (0 to stop): ")
    if value=="0":
        break
    print("You entered:", value)

#7
items="pen book pencil"
for item in items.split():
    if item == "phone":
        print("Match found")
        break
else:
    print("All items checked; no match found")

#8
age = 16
if age >= 18:
    pass
else:
    print("Under 18")
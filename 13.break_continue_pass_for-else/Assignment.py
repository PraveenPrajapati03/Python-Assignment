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

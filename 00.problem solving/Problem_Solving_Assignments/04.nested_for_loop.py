# Level 1 — Nested Loop Basics
# 1
for i in range(1,4):
    for j in range(1,4):
        print(i,j)

# 2
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        print(f"{i} X {j} = {i*j}")

# 3
character=input("Enter character :")
rows=int(input("Enter number of rows :"))
columns=int(input("Enter number of columns :"))
for i in range(rows):
    for j in range(columns):
        print(character,end="")
    print()

# 4
rows=int(input("Enter number of rows :"))
columns=int(input("Enter number of columns :"))
for i in range(rows):
    for j in range(columns):
        print(f"{(i,j)}",end=" ")
    print()

# 5
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        print(i,end="")
    print()

# 6
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        print(j,end="")
    print()

# 7
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# 8
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N-i+2):
        print(j,end="")
    print()

# 9
rows=int(input("Enter number of rows :"))
columns=int(input("Enter number of columns :"))
for i in range(rows):
    for j in range(columns):
        print("*",end="")
    print()

# 10
N=int(input("Enter number :"))
for i in range(N):
    for j in range(N):
        if j%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()



# Level 2 — Conditions Inside Nested Loops
# 11
rows=int(input("Enter number of rows :"))
columns=int(input("Enter number of columns :"))
for i in range(1,rows+1):
    for j in range(1,columns+1):
        if j%2==0:
            print(j,end=" ")
    print()

# 12
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if j%2!=0:
            print(j,end=" ")
    print()

# 13
for i in range(1,5):
    for j in range(1,5):
        if (i+j)%2==0:
            print("E",end=" ")
        else:
            print("O",end=" ")
    print()

# 14
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print("Same",end=" ")
        else:
            print("Different",end=" ")
    print()

# 15
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

# 16
for i in range(1,6):
    for j in range(1,6):
        if i%j==0:
            print("X",end=" ")
        else:
            print("-",end=" ")
    print()

# 17
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if j%i==0:
            print(j,end=" ")
    print()

# 18
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i+j>N:
            print(i,j)

# 19
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i*j%2==0:
            print(i,j,i*j)

# 20
N=int(input("Enter number :"))
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print("SPECIAL",end=" ")
        elif i+j==N:
            print("PAIR",end=" ")
        else:
            print("NORMAL",end=" ")
    print()



# Level 3 — Strings + Nested Loops
# 21
string=input("Enter string :")
for character in string:
    print(character*3)

# 22
string=input("Enter string :")
for character in string:
    for i in range(3):
        print(character,i)

# 23
string=input("Enter string :")
for i in string:
    for j in string:
        if i==j:
            print("Same",end=" ")
        else:
            print("Different",end=" ")
    print()


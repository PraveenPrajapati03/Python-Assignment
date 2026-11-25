# # Level 1 — Nested Loop Basics
# # 1
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

# # 2
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(f"{i} X {j} = {i*j}")

# # 3
# character=input("Enter character :")
# rows=int(input("Enter number of rows :"))
# columns=int(input("Enter number of columns :"))
# for i in range(rows):
#     for j in range(columns):
#         print(character,end="")
#     print()

# # 4
# rows=int(input("Enter number of rows :"))
# columns=int(input("Enter number of columns :"))
# for i in range(rows):
#     for j in range(columns):
#         print(f"{(i,j)}",end=" ")
#     print()

# # 5
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(i,end="")
#     print()

# # 6
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(j,end="")
#     print()

# # 7
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# # 8
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N-i+2):
#         print(j,end="")
#     print()

# # 9
# rows=int(input("Enter number of rows :"))
# columns=int(input("Enter number of columns :"))
# for i in range(rows):
#     for j in range(columns):
#         print("*",end="")
#     print()

# # 10
# N=int(input("Enter number :"))
# for i in range(N):
#     for j in range(N):
#         if j%2==0:
#             print(0,end="")
#         else:
#             print(1,end="")
#     print()



# # Level 2 — Conditions Inside Nested Loops
# # 11
# rows=int(input("Enter number of rows :"))
# columns=int(input("Enter number of columns :"))
# for i in range(1,rows+1):
#     for j in range(1,columns+1):
#         if j%2==0:
#             print(j,end=" ")
#     print()

# # 12
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if j%2!=0:
#             print(j,end=" ")
#     print()

# # 13
# for i in range(1,5):
#     for j in range(1,5):
#         if (i+j)%2==0:
#             print("E",end=" ")
#         else:
#             print("O",end=" ")
#     print()

# # 14
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")
#     print()

# # 15
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i==j:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

# # 16
# for i in range(1,6):
#     for j in range(1,6):
#         if i%j==0:
#             print("X",end=" ")
#         else:
#             print("-",end=" ")
#     print()

# # 17
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if j%i==0:
#             print(j,end=" ")
#     print()

# # 18
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i+j>N:
#             print(i,j)

# # 19
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i*j%2==0:
#             print(i,j,i*j)

# # 20
# N=int(input("Enter number :"))
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i==j:
#             print("SPECIAL",end=" ")
#         elif i+j==N:
#             print("PAIR",end=" ")
#         else:
#             print("NORMAL",end=" ")
#     print()



# # Level 3 — Strings + Nested Loops
# # 21
# string=input("Enter string :")
# for character in string:
#     print(character*3)

# # 22
# string=input("Enter string :")
# for character in string:
#     for i in range(3):
#         print(character,i)

# # 23
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")
#     print()

# # 24
# string1=input("Enter first string :")
# string2=input("Enter second string :")
# for i in string1:
#     for j in string2:
#         if i==j:
#             print(i,j)

# # 25
# string1=input("Enter first string :")
# string2=input("Enter second string :")
# count=0
# for i in string1:
#     for j in string2:
#         if i==j:
#             count+=1
# print(count)

# # 26
# string=input("Enter string :")
# for i in range(len(string)):
#     count=0
#     for j in string:
#         if string[i]==j:
#             count+=1
#     flag=True
#     for k in range(1,i-1):
#         if string[i]==string[k]:
#             flag=False
#     if flag:
#         print(f"{string[i]} = {count}")

# # 27
# string=input("Enter string :")
# for i in string:
#     if i in "AEIOUaeiou":
#         print(f"{i} = Vowel")
#     else:
#         print(f"{i} = Consonant")

# # 28
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# for i in range(len(string1)):
#     flag = True
#     for j in string2:
#         if string1[i] == j:
#             for k in range(i):
#                 if string1[k] == string1[i]:
#                     flag = False
#             if flag:
#                 print(string1[i])
#             break

# # 29
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         print(i,j)

# # 30
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         if i==j:
#             continue
#         else:
#             print(i,j,end=", ")



# # Level 4 — Strings + Conditions + ASCII
# # 31
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         if i==j:
#             print("Same",end=" ")
#         else:
#             print("Different",end=" ")
#     print()

# # 32
# string=input("Enter string :")
# for i in string:
#     if i in "AEIOUaeiou":
#         for j in string:
#                 if j not in "AEIOUaeiou":
#                     print(f"{i}-{j}",end=", ")

# # 33
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         if i.isupper() and j.isupper():
#             print(i,j,end=" ")
#         elif i.isupper() or j.isupper():
#             continue
#         else:
#             print(i,j,end=" ")
#     print()

# # 34
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         if i==j:
#             continue
#         else:
#             if ord(i)-ord(j)>0:
#                 print(f"{i} {j} -> {ord(i)-ord(j)}",end=", ")
#             else:
#                 print(f"{i} {j} -> {ord(j)-ord(i)}",end=", ")
#     print()

# # 35
# string=input("Enter string :")
# for i in string:
#     for j in string:
#         if i==j:
#             continue
#         else:
#             if ord(i)-ord(j)>0:
#                 print(f"{i}->{j} Decreasing",end=", ")
#             else:
#                 print(f"{i}->{j} Increasing",end=", ")
#     print()



# # Level 5 — split() + Nested Loops (SKIP)
# # 36
# sentence=input("Enter sentence :")
# words=sentence.split()
# for i in words:
#     for j in words:
#         if i==j:
#             continue
#         else:
#             print(i,j)

# # 37
# sentence=input("Enter sentence :")
# words=sentence.split()
# for i in words:
#     for j in words:
#         if len(i)==len(j) and i!=j:
#             print(i,j)

# # 38
# sentence=input("Enter sentence :")
# words=sentence.split()
# for i in words:
#     for j in words:
#         if i[0]==j[0] and i!=j:
#             print(i,j)

# # 39
# sentence=input("Enter sentence :")
# words=sentence.split()
# for i in words:
#     for j in words:
#         if i[len(i)-1]==j[len(j)-1] and i!=j:
#             print(i,j)

# # 40
# sentence = input("Enter sentence :")
# words = sentence.split()
# for i in words:
#     for j in words:
#         if i != j:
#             for k in i:
#                 for m in j:
#                     if k == m:
#                         print(i, j)
#                         break
#                 else:
#                     continue
#                 break

# # 41
# sentence=input("Enter sentence :")
# words=sentence.split()
# for i in words:
#     for j in words:
#         if len(i)>len(j) and len(i)!=len(j) and i!=j:
#             print(i,j,len(i)-len(j))
#         elif len(i)<len(j) and len(i)!=len(j) and i!=j:
#             print(i,j,-(len(i)-len(j)))

# # 42
# sentence=input("Enter sentence :")
# words=sentence.split()
# lword=""
# sword=""
# for i in words:
#     if len(lword)<len(i):
#         lword=i
#     if 1>=len(i):
#         sword=i
# print("Longest =",lword)
# print("Shortest =",sword)



# # Level 6 — Dynamic Nested Loops
# # 43
# N=int(input("Enter number of rows :"))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print() 

# # 44
# N=int(input("Enter number of rows :"))
# for i in range(1,N+1):
#     for j in range(N-i+1,0,-1):
#         print(j,end=" ")
#     print() 

# # 45
# N=int(input("Enter number of rows :"))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(j*i,end=" ")
#     print() 

# 46
  
# Nested For Loops – Basic Python Problems
# 1. Print a 3×3 Star Grid
for row in range(3):
    for coloum in range(3):
        print("*",end=" ")
    print()    


# 2. Print Numbers in Rows
for row in range(3):
    for coloum in range(3):
        print(coloum+1,end=" ")
    print()  


# 3. Print Row Numbers
for row in range(3):
    for coloum in range(3):
        print(row+1,end=" ")
    print() 


# 4. Increasing Star Pattern
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()    


# 5. Decreasing Star Pattern
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()


# 6. Increasing Number Pattern
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()    


# 7. Repeated Number Pattern
for i in range(5):
    for j in range(i+1):
        print(i+1,end=" ")
    print()


# 8. Multiplication Tables from 1 to 5
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}x{j}=>{i*j}")
    print()    


# 9. Multiplication Grid
for i in range(1,4):
    for j in range(1,6):
        print(i*j,end=" ")
    print()    


# 10. Print Squares in Rows
for i in range(1,6):
    for j in range(1,6):
        print(j**2,end=" ")
    print()    


# 11. Alphabet Pattern
for i in range(5):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()    


# 12. Repeated Alphabet Pattern
for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()  


# 13. Odd Number Pattern
for i in range(5):
    for j in range(0,(i+1)*2,2):
        print((j+1),end=" ")
    print()    


# 14. Even Number Pattern
for i in range(5):
    for j in range(1,(i+1)*2,2):
        print((j+1),end=" ")
    print()    


# 15. 5×5 Star Square
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()    


# 16. 5×5 Number Square
for i in range(5):
    for j in range(5):
        print(j+1,end=" ")
    print()


# 17. Row-wise Numbers
number=1
for i in range(3):
    for j in range(3):
        print(number,end=" ")
        number+=1
    print()    


# 18. Print 1 to 20 in 4 Rows
number=1
for i in range(4):
    for j in range(5):
        print(number,end=" ")
        number+=1
    print()    


# 19. Print Coordinate Pair
for i in range(1,4):
    for j in range(1,4):
        print(f"({i},{j})",end=" ")
    print()    


# 20. Print All Number Combinations
for i in range(1,4):
    for j in range(1,4):
        print(i,j)


# 21. 10×10 Multiplication Grid
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}=>{i*j}",end=" ")
    print()    


# 22. Repeated Number Pattern
for i in range(5):
    for j in range(i+1):
        print(1+i,end="")
    print()    


# 23. Decreasing Number Pattern
for i in range(5):
    for j in range(4-i+1):
        print(j+1,end="")
    print()


# 24. Reverse Number Pattern
for i in range(5):
    for j in range(4-i+1):
        print(5-j,end="")
    print()    


# 25. Repeated Row Number Pattern
for i in range(5):
    for j in range(5):
        print(i+1,end="")
    print()    
# #Python Mixed Problem-Solving — 50 Unique Questions
# #1. Digit and Character Analyzer
# string=input("Enter paragraph:")
# ucount=lcount=dcount=scount=sccount=0
# for i in string:
#     if chr(65)<=i<=chr(90):
#         ucount+=1
#     elif chr(97)<=i<=chr(122):
#         lcount+=1    
#     elif chr(48)<=i<=chr(57):
#         dcount+=1    
#     elif i==chr(32):
#         scount+=1    
#     else:
#         sccount+=1 
# if ucount>lcount and ucount>dcount and ucount>scount and ucount>sccount:
#     print("In string upper case characters is highest:",ucount)
# elif lcount>ucount and lcount>dcount and lcount>scount and lcount>sccount:
#     print("In string lower case characters is highest:",lcount)    
# elif dcount>ucount and dcount>lcount and dcount>scount and dcount>sccount:
#     print("In string digits is highest:",dcount)    
# elif scount>ucount and scount>lcount and scount>dcount and scount>sccount:
#     print("In string spaces is highest:",scount)     
# elif sccount>ucount and sccount>lcount and sccount>dcount and sccount>scount:
#     print("In string special characters is highest:",sccount)     
# else:
#     print("Tie")



# #2. Student Performance Analyzer
# fcount=pcount=gcount=ecount=0
# for i in range(10):
#     marks=int(input("Enter marks:"))
#     if 100>=marks>=75:
#         ecount+=1
#         print("Excellent")
#     elif 74>=marks>=50:
#         gcount+=1
#         print("Good")    
#     elif 49>=marks>=35:
#         pcount+=1
#         print("Pass")
#     elif 0<=marks<35:
#         fcount+=1
#         print("Fail")        
#     else:
#         print("please enter marks in range 0 to 100")
# print("In Excellent category number of students is:",ecount)
# print("In Good category number of students is:",gcount)
# print("In Pass category number of students is:",pcount)
# print("In Fail category number of students is:",fcount)



# #3. Word Score Calculator
# string=input("Enter paragraph:")
# letters=string.split()
# highest_score=0
# highest_score_word=""
# for letter in letters:
#     score=0
#     for i in letter:
#         if i in "AEIOUaeiou":
#             score+=2
#         elif "A" <= i <= "Z" or "a" <= i <= "z":
#             score+1
#         elif chr(48)<=i<=chr(57):
#             score+=3  
#         else:
#             score+=4
#     if highest_score<score:
#         highest_score=score
#         highest_score_word=letter
# print("Highest scoring word is:",highest_score_word)          
# print("Score:", highest_score)



# #4. Password Batch Validator
# for i in range(5):
#     ucount=lcount=dcount=sccount=islen=False
#     passwords=input("Enter password:")
#     for char in passwords:
#         if len(passwords)>=8:
#             islen=True
#         if chr(65)<=char<=chr(90):
#             ucount=True
#         elif chr(97)<=char<=chr(122):
#             lcount=True
#         elif chr(48)<=char<=chr(57):
#             dcount=True
#         else:
#             sccount=True  
#     score=int(islen)+int(ucount)+int(lcount)+int(dcount)+int(sccount)      
#     if score>=5:
#         print("Password is Strong") 
#     elif score>=3:
#         print("Password is Medium")    
#     else:
#         print("Password is Weak")      



# #5. Sentence Word Analyzer
# Sentence=input("Enter Sentence:")
# words=Sentence.split()
# short_count=medium_count=long_count=0
# for word in words:
#     word_char_count=0
#     print("The length of",word,"is",len(word))
#     for i in word:
#         word_char_count+=1
#     if word_char_count<=3:
#         short_count+=1
#         print("word is short")
#     elif word_char_count<6:
#         medium_count+=1
#         print("medium")    
#     else:
#         long_count+=1
#         print("long")    
# print("The short word in sentance is:",short_count)        
# print("The medium word in sentance is:",medium_count)        
# print("The long word in sentance is:",long_count)        



# #6. Number-String Conversion Challenge
# for i in range(5):
#     num=int(input("Enter number:"))
#     snum=str(num)
#     ecount=ocount=0
#     for digit in snum:
#         if int(digit)%2==0:
#             ecount+=1
#         else:
#             ocount+=1        
#     if ecount>ocount:
#         print("in string number even number is more") 
#     elif ecount<ocount:
#         print("in string number odd number is more")   
#     else:
#         print("in string number even number or odd number are equal")



# #7. Repeated Character Report
# string=input("Enter paragraph:")
# for char in string:
#     count=0
#     for i in string:
#         if char==i:
#             count+=1
#     if count>1:        
#         if count==2:
#             print(char, ":", count, "Duplicate")
#         elif 3<=count<=4:
#             print(char, ":", count, "Repeated")   
#         else:
#             print(char, ":", count, "Highly Repeated")     



# #8. Shopping Cart Analyzer
# total_price=0
# budget_count=regular_count=premium_count=luxury_count=0
# for i in range(8):
#     price=float(input("Enter price:"))
#     total_price+=price
#     if price<500:
#         budget_count+=1
#         print("Budget")
#     elif price<2000:
#         regular_count+=1
#         print("Regular")    
#     elif price<5000:
#         premium_count+=1
#         print("Premium")   
#     else:
#         luxury_count+=1
#         print("Luxury")    
# avg=total_price/8
# print("The total price is:",total_price)    
# print("no of items in Budget price is:",budget_count)             
# print("no of items in regular price is:",regular_count)             
# print("no of items in premium price is:",premium_count)             
# print("no of items in luxury price is:",luxury_count)    
# print("Average product price is:",avg)         



# #9. Character Position Challenge
# string=input("Enter paragraph:")
# position=0
# vowel_count=consonant_count=digit_count=specialchar_count=0
# for i in string:
#     print("character is:",i,"there position is:",position,end=" ")
#     if position%2==0:
#         print("position is even",end=" ")
#     else:
#         print("position is odd",end=" ")
#     if i in "AEIOUaeiou":
#         vowel_count+=1
#         print("and character is vowel")
#     elif "A" <= i <= "Z" or "a" <= i <= "z":
#         consonant_count+= 1
#         print("and character is consonant")
#     elif chr(48)<=i<=chr(57):
#         digit_count+=1  
#         print("and character is digit")
#     else:
#         specialchar_count+=1  
#         print("and character is special")
#     position+=1    
# print("in string vowel is:",vowel_count)              
# print("in string consonant is:",consonant_count)              
# print("in string digit is:",digit_count)              
# print("in string special character is:",specialchar_count)              



# #10. Number Pattern With Conditions
# n=int(input("Enter number of rows:"))
# for i in range(n):
#     for j in range(1,i*2+2):
#         if (j)%3==0 and (j)%5==0:
#             print("Z",end=" ")
#         elif (j)%3==0:
#             print("X",end=" ") 
#         elif (j)%5==0:
#             print("Y",end=" ") 
#         else:   
#             print(j,end=" ")
#     print()    




# #12. Vowel-Consonant Battle
# sentence=input("Enter sentence:")
# vowel_count=consonant_count=0
# acount=ecount=icount=ocount=ucount=0
# for i in sentence:
#     if i in "Aa":
#         acount+=1
#         vowel_count+=1
#     elif i in "Ee":
#         ecount+=1
#         vowel_count+=1
#     elif i in "Ii":
#         icount+=1
#         vowel_count+=1   
#     elif i in "Oo":
#         ocount+=1
#         vowel_count+=1 
#     elif i in "Uu":
#         ucount+=1
#         vowel_count+=1        
#     else:
#         consonant_count+=1
# if vowel_count>consonant_count:
#     print("Vowels Win")   
# elif vowel_count<consonant_count:
#     print("Consonants Win")         
# else:
#     print("Draw")  
# print("in string a and A letters frequency is:",acount)              
# print("in string e and E letters frequency is:",ecount)              
# print("in string i and I letters frequency is:",icount)              
# print("in string o and O letters frequency is:",ocount)              
# print("in string u and U letters frequency is:",ucount)      



# #13. Electricity Bill Calculator
# for i in range(6):
#     units_used=int(input("Enter units used:"))
#     total_revenue=0
#     if units_used<=100:
#         total_revenue=units_used*5
#     elif units_used<=200:
#         total_revenue=100*5+(units_used-100)*7
#     elif units_used<=400:
#         total_revenue=100*5+100*7+(units_used-200)*10
#     else:
#         total_revenue=100*5+100*7+200*10+(units_used-400)*15
#     print("total revenue is:",total_revenue)    
#     if total_revenue<1000:
#         print("Low")      
#     elif total_revenue<3000:
#         print("Medium")   
#     else:
#         print("High")    



# #14. Word Character Balance
# sentence=input("Enter sentence:")
# words=sentence.split()
# for word in words:
#     vowel_count=consonant_count=other_count=0
#     for i in word:
#         if i in "AEIOUaeiou":
#             vowel_count+=1
#         elif "A" <= i <= "Z" or "a" <= i <= "z":
#             consonant_count+=1
#         else:
#             other_count+=1  
#     if vowel_count>consonant_count:
#         print(f"In this word {word}: Vowel Heavy")   
#     elif vowel_count<consonant_count:
#         print(f"In this word {word}: Consonant Heavy")         
#     else:
#         print(f"In this word {word}: Balanced")



# #15. Matrix Value Analyzer
# row1=""
# row2=""
# row3=""
# for i in range(3):
#     for j in range(3):
#         if i==0:
#             elements=int(input(f"Enter matrix elements for row 1 and coloum {j+1}:"))
#             row1=str(elements)+row1
#         elif i==1:
#             elements=int(input(f"Enter matrix elements for row 2 and coloum {j+1}:"))
#             row2=str(elements)+str(row2)              
#         else:
#             elements=int(input(f"Enter matrix elements for row 3 and coloum {j+1}:"))
#             row3=str(elements)+str(row3)     
# print("matrix is:")              
# print(row1)        
# print(row2)        
# print(row3) 
# matrix=row1+row2+row3
# print(matrix)       




# #16. Password Character Distribution
# password=input("Enter password:")
# ucount=lcount=dcount=sccount=0
# for i in password:
#     if chr(65)<=i<=chr(90):
#         ucount+=1
#     elif chr(97)<=i<=chr(122):
#         lcount+=1    
#     elif chr(48)<=i<=chr(57):
#         dcount+=1    
#     else:
#         sccount+=1 
# total_char=ucount+lcount+dcount+sccount
# print(f"The upper character percantage in password is: {(ucount/total_char)*100}")
# print(f"The lower character percantage in password is: {(lcount/total_char)*100}")
# print(f"The digit character percantage in password is: {(dcount/total_char)*100}")
# print(f"The special character percantage in password is: {(sccount/total_char)*100}")
# if (ucount/total_char)*100>(lcount/total_char)*100 and (ucount/total_char)*100>(dcount/total_char)*100 and (ucount/total_char)*100>(sccount/total_char)*100:
#     print("upper characters dominates")
# elif (lcount/total_char)*100>(ucount/total_char)*100 and (lcount/total_char)*100>(dcount/total_char)*100 and (lcount/total_char)*100>(sccount/total_char)*100:
#     print("lower characters dominates")    
# elif (dcount/total_char)*100>(lcount/total_char)*100 and (dcount/total_char)*100>(ucount/total_char)*100 and (dcount/total_char)*100>(sccount/total_char)*100:
#     print("digits dominates") 
# else:
#     print("special charcters dominates")  



# #17. Student Name and Marks
# high_marks=0
# topper=""
# for i in range(5):
#     vowel_count=consonant_count=0
#     grade=""
#     student_name=input("Enter your name:")
#     for word in student_name:
#         if word in "AEIOUaeiou":
#             vowel_count+=1
#         elif "A" <= word <= "Z" or "a" <= word <= "z":
#             consonant_count+=1    
#     marks=int(input("Enter your marks:"))    
#     if 100>=marks>=90:
#         grade="A+"
#     elif 89>=marks>=75:
#         grade="A"  
#     elif 74>=marks>=50:
#         grade="B"
#     elif 35<=marks<50:
#         grade="C"
#     elif 0<=marks<=34:
#         grade="D"
#     else:
#         print("please marks give in range 0 to 100")  
#     print("student get grade is:",grade)          
#     if vowel_count>consonant_count:
#         print("In students name vowel is more than consonant")      
#     else:
#         print("In students name consonant is more than vowel")          
#     if high_marks<marks:
#         high_marks=marks
#         topper=student_name  
# print(f"the topper in 5 students is {topper} and get marks is:{high_marks}")    



# #18. ATM Transaction Analyzer
# balance=float(input("Enter present balance:"))
# transaction_count=0
# for i in range(7):
#     Deposit_transaction=int(input(f"Enter number of Deposit in day{i+1}:"))
#     Withdrawal_transaction=int(input(f"Enter number in Withdrawal in day{i+1}:"))
#     for j in range(Deposit_transaction):
#         deposit_money=float(input(f"Enter deposit {j+1} money:"))
#         transaction_count+=1
#         balance+=deposit_money
#     for k in range(Withdrawal_transaction):
#         withdrawal_money=float(input(f"Enter withdrawal {k+1} money:"))
#         if withdrawal_money>balance:
#             print("not enogh money")
#         else:
#             balance-=withdrawal_money
#             transaction_count+=1
#         if balance<1000:
#             print("Low Balance")     
# print("final balance is:",balance)
# print("the total number of transactions is:",transaction_count)       



#19. Sentence Security Scanner
sentence=input("Enter sentence:")
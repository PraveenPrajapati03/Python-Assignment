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



# #11. Username Analyzer
# for i in range(5):
#     is_len=is_first_char=is_digit=is_underscore=is_invalid_schar=False
#     digit_count=underscore_count=0
#     user_name=input("Enter your user name:")
#     if len(user_name)>=8:
#         is_len=True
#     first_char=user_name[0]   
#     if chr(65)<=first_char<=chr(90):
#         is_first_char=True
#     for i in user_name:
#         if chr(48)<=i<=chr(57):    
#             digit_count+=1
#             is_digit=True
#         elif i==chr(95):   
#             underscore_count+=1
#             is_underscore=True
#         else:
#             is_invalid_schar=True
#     score=int(is_len)+int(is_first_char)+int(is_digit)+int(is_underscore)+int(is_invalid_schar) 
#     if score==5:
#         print("Valid")    
#     elif 3<=score<=4:
#         print("Needs Improvement")    
#     else:
#         print("Invalid")    
#     print("the length of username is:",len(user_name))    
#     print("number of digit in username is:",digit_count)
#     print("number of underscore in username is:",underscore_count)
            


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
# even_count=odd_count=positive_count=negative_count=zero_count=large_num=0
# for i in range(3):
#     for j in range(3):
#         num=int(input(f"Enter number for matrix (rows x coloums) {i+1}x{j+1}:"))
#         if num%2==0:
#             even_count+=1
#         else:
#             odd_count+=1
#         if num>0:
#             positive_count+=1
#         elif num<0:
#             negative_count+=1
#         else:
#             zero_count+=1
#         if large_num<num:
#             large_num=num
# print("even number in matrix is:",even_count)      
# print("odd number in matrix is:",odd_count)      
# print("positive number in matrix is:",positive_count)      
# print("negative number in matrix is:",negative_count)      
# print("zero number in matrix is:",zero_count)     
# print("largest number in matrix is:",large_num) 
        
# #15.extra concept
# matrix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     ]

# matrix=[]
# for i in range(3):
#     arr = list(map(int,input("Enter the Number: ").split()))
#     matrix.append(arr)
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




# #20. Multiplication Grid Analyzer
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i*j%5==0:
#             print("F",end=" ")
#         elif j*i%2==0:
#             print("E",end=" ")
#         else:
#             print("O",end=" ")
#     print()                



# #21. Shopping Discount System
# final_price=discount_price=0
# count_20=count_15=count_10=count_0=0
# for i in range(10):
#     product_price=int(input("Enter prices:"))
#     if product_price>=5000:
#         discount_price+=product_price*0.2
#         final_price+=product_price-product_price*0.2
#         count_20+=1
#     elif product_price>=3000:
#         discount_price+=product_price*0.15
#         final_price+=product_price-product_price*0.15
#         count_15+=1
#     elif product_price>=1000:
#         discount_price+=product_price*0.1
#         final_price+=product_price-product_price*0.1
#         count_10+=1
#     else:
#         discount_price+=0
#         final_price+=product_price
#         count_0+=1
# print("The final price you will pay:",final_price)
# print("The total discount price is:",discount_price)
# print("The number of product price get 20% discount are:",count_20)
# print("The number of product price get 15% discount are:",count_15)
# print("The number of product price get 10% discount are:",count_10)
# print("The number of product price get 0% discount are:",count_0)



# #22. String Compression Counter
# sentence = input("Enter sentence:")
# a=0
# for i in sentence:
#     count = 0
#     for j in sentence:
#         if i==j:
#             count += 1
#     already_printed = False
#     for k in range(a):  
#         if i == sentence[k]:
#             already_printed = True 
#     a+=1                           
#     if count > 1 and not already_printed:
#         print(i+str(count),end="")



# #23. Employee Salary Analyzer
# total_salaries=executive_count=senior_count=mid_count=junior_count=0
# for i in range(8):
#     salary=int(input("Enter your salary:"))
#     if salary>100000:
#         print("Executive")
#         total_salaries+=salary
#         executive_count+=1
#     elif salary>50000:
#         print("Senior")
#         total_salaries+=salary
#         senior_count+=1
#     elif salary>=25000:
#         print("Mid")    
#         total_salaries+=salary
#         mid_count+=1
#     else:
#         print("Junior")    
#         total_salaries+=salary
#         junior_count+=1
# print("The number of junior is:",junior_count) 
# print("The number of mid is:",mid_count) 
# print("The number of senior is:",senior_count) 
# print("The number of executive is:",executive_count) 
# avg_salary=total_salaries/8
# print("The avrage salary is:",avg_salary)



# #24. Secret Word Detector
# sentence = input("Enter a sentence:")
# secret = input("Enter secret word:")
# words=sentence.split()
# word_count=0
# position_found = False
# current_position = 0
# position=0
# for word in words:
#     if word==secret:
#         word_count+=1
#         if position_found == False:
#             position = current_position
#             position_found = True
#     current_position += len(word) + 1      
# if word_count==0:
#     print("Secret word not found")    
# else:
#     print("The number of secret word found is:",word_count)
#     print("Starting position:",position)    
# #24. or adavance type solve
# sentence=input("Enter a sentence and a secret word:")
# words=sentence.split()
# word_count=0
# starting_position_flag=True
# starting_position=0
# for index,word in enumerate(words):
#     if word=="praveen":
#         if starting_position_flag:
#             starting_position=index
#             starting_position_flag=False
#         word_count+=1
# if word_count==0:
#     print("Secret word not found")    
# else:
#     print("The number of secret word found is:",word_count, starting_position)                



# #25. Number Pyramid With Classification
# n=int(input("Enter number:"))
# for i in range(1,n+1):
#     for s in range(n-i):
#         print(" ",end="")
#     for j in range(1,i*2):
#         if j%3==0 and j%5==0:
#             print("F",end="")
#         elif j%3==0:
#             print("T",end="")
#         elif j%2==0:
#             print("E",end="")
#         else:
#             print("O",end="")                
#     print()   



# #26. Movie Rating Analyzer
# pcount=acount=gcount=ecount=ocount=total_rating=0
# for i in range(10):
#     give_rating=float(input("Enter movie rating out of 10:"))
#     if give_rating>9:
#         print("Outstanding")
#         ocount+=1
#         total_rating+=give_rating
#     elif give_rating>7:
#         print("Excellent") 
#         ecount+=1
#         total_rating+=give_rating   
#     elif give_rating>5:
#         print("Good")  
#         gcount+=1  
#         total_rating+=give_rating
#     elif give_rating>3:
#         print("Average")  
#         acount+=1  
#         total_rating+=give_rating
#     else:
#         print("Poor")    
#         pcount+=1
#         total_rating+=give_rating
# print("The number of movie got Outstanding rating is:",ocount)        
# print("The number of movie got Excellent rating is:",ecount)        
# print("The number of movie got Good rating is:",gcount)        
# print("The number of movie got Average rating is:",acount)        
# print("The number of movie got Poor rating is:",pcount)        
# print("The average rating of movie is:",total_rating/10)



# #27. Word Frequency Without Dictionary
# sentence = input("Enter sentence:")
# words=sentence.split()
# a=0
# for i in words:
#     count = 0
#     for j in words:
#         if i==j:
#             count += 1
#     already_printed = False
#     for k in range(a):  
#         if i == words[k]:
#             already_printed = True 
#     a+=1                           
#     if count > 1 and not already_printed:
#         print(f"The word {i} is appearing:{count} times")
# #or
# sentence = input("Enter sentence:")
# words = sentence.split()
# for i in range(len(words)):
#     count = 0
#     for j in range(len(words)):
#         if words[i] == words[j]:
#             count += 1
#     already_printed = False
#     for k in range(i):
#         if words[i] == words[k]:
#             already_printed = True
#     if count > 1 and not already_printed:
#         print(words[i], count)


 
# #28. Number With Maximum Even Digits
# high_even_count=0
# high_even_count_number=0
# for i in range(10):
#     num=int(input("Enter number:"))
#     snum=str(num)
#     even_count=odd_count=0
#     for digit in snum:
#         if int(digit)%2==0:
#             even_count+=1
#         else:
#             odd_count+=1    
#     if even_count>high_even_count:
#         high_even_count=even_count
#         high_even_count_number=num
#     if even_count==odd_count:
#         print("the tied number is:",num)
# print("the number has highest number of even number is:",high_even_count_number,"in this number even number is:",high_even_count)        



# #29. Email Validator baki
# flag=True
# for i in range(5):
#     email=input("Enter email:")
#     if "a"<=email[0]<="z" or "A"<=email[0]<="Z":
#         for word in email:
#             if word=="@":
#                 count_a+=1
#             elif word==" ":
#                 print("Invalid")
#     else:
#         print("Invalid")        




# #34. Number Triangle With Prime Check
# n=int(input("Enter number:"))
# for i in range(1,n+1):    
#     for j in range(1,i+1):
#         count=0
#         for k in range(1,j+1):
#             if j%k==0:
#                 count+=1
#         if count==2:
#             print("P",end="")     
#         elif j%2==0:
#             print("E",end="")
#         else:
#             print("O",end="")                
#     print()    


# #37. Character Pyramid
# sentence = input("Enter a sentence:")
# for i in range(len(sentence)):
#     for j in range(i+1):
#         print(sentence[j],end="") 
#     print()    
# for i in range(len(sentence)):
#     for j in range(len(sentence)-i):
#         print(sentence[j],end="") 
#     print()    



# #46. Number Box Pattern
# n=int(input("Enter number of rows and colums for n*n box:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1:
#             print("*",end="")  
#         elif 1<i<n:
#             if (i+j)%2==0 and 1<j<n:
#                 print("E",end="")
#             elif (i+j)%2!=0 and 1<j<n:
#                 print("O",end="") 
#             else:
#                 print("*",end="") 
#         else:
#             print("*",end="")   
#     print()                   



#50. Complete Data Analyzer Challenge
for i in range(10):
    string=input("Enter paragraph:")
    ucount=lcount=dcount=scount=sccount=0
    words=string.split()
    a=0
    longest_word=""
    for j in words:
        for i in j:
            if chr(65)<=i<=chr(90):
                upper_count+=1
            elif chr(97)<=i<=chr(122):
                lower_count+=1
            if i in "AEIOUaeiou":
                vowel_count+=1
                score+=2
            elif "A" <= i <= "Z" or "a" <= i <= "z":
                consonant_count+=1
                score+1
            elif chr(48)<=i<=chr(57):
                digit_count+=1
                score+=3  
            elif i==chr(32):
                score+=0 
                space_count+=1   
            else:
                score+=4
                special_count+=1  
        if len(j)>len(longest_word):
            longest_word=j                           
    a=0
    for i in string:
        count = 0
        for j in string:
            if i==j:
                count += 1
        already_printed = False
        for k in range(a):  
            if i == string[k]:
                already_printed = True 
        a+=1                           
        if count > 1 and not already_printed:
            print(i+str(count),end="")            
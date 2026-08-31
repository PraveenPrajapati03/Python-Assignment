#Part 3 — String Creation and Basic Operations
#Task 1 — Create Strings
your_name='Praveen Prajapati'
your_city='Nagaur'
favorite_language="Python"
message="my name is praveen prajapati form nagaur rajasthan and i am btech cse student at coding gita"
print("Output for task 1:.................................................")
print(your_name,your_city,favorite_language,message)

#Task 2 — Empty String
a=""
print("Output for task 2:.................................................")
print(a,len(a),type(a))

#Task 3 — String Information
a="Python Programming"
print("Output for task 3:.................................................")
print(a[:])
print(len(a))
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])

#Part 4 — Indexing
#Task 4 — Positive Indexing
a="Programming"
print("Output for task 4:.................................................")
print(a[0])
print(a[1])
print(a[4])
print(a[-1])

#Task 5 — Negative Indexing
a="Programming"
print("Output for task 5:.................................................")
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-11])

#Task 6 — Indexing Challenge
name="Praveen Prajapati"
print("Output for task 6:.................................................")
print(name[0])
print(name[-1])
print(name[8])

#Part 5 — Slicing
#Task 7 — Basic Slicing
a="Python Programming"
print("Output for task 7:.................................................")
print(a[0:6])
print(a[7:])
print(a[:])
print(a[0:5])
print(a[-5:])

#Task 8 — Slicing with Step
a="ABCDEFGHIJKL"
print("Output for task 8:.................................................")
print(a[::2])
print(a[::3])
print(a[1:9:2])
print(a[::-1])

#Task 9 — Slicing with Negative Indexes
a="Python Programming"
print("Output for task 9:.................................................")
print(a[-5:])
print(a[-10:])
print(a[::-1])

#Task 10 — Slicing Challenge
a="Praveen Prajapati"
print("Output for task 10:.................................................")
print(a[0:3])
print(a[-3:])
print(a[::2])
print(a[::-1])
print(a[1:16])

#Part 6 — Length
#Task 11
a="Praveen"
b="my name is praveen prajapati form nagaur rajasthan"
c="""Rajasthan translates literally from Sanskrit to English as "The Land of Kings" or "The Abode of the Rajas". It is a portmanteau of Rājā (meaning King) and Sthāna (meaning Land). Before India's independence, the British referred to this region as Rajputana, meaning "The Country of the Rajputs"."""
print("Output for task 11:.................................................")
print(len(a))
print(len(b))
print(len(c))

#Task 12
text = "Python Programming"
print("Output for task 12:.................................................")
a=len(text)
b=a-1
print(a)
print(text[b])

#Part 7 — Concatenation
#Task 13 — Full Name
fisrt_name="Praveen"
last_name="Prajapati"
print("Output for task 13:.................................................")
print(fisrt_name+" "+last_name)

#Task 14 — Sentence Creation
name="Praveen"
age="18"
city="Nagaur"
Programming_language="Python"
print("Output for task 14:.................................................")
print(name+age+city+Programming_language)

#Task 15 — String and Integer
a="praveen"
b="18"
print("Output for task 15:.................................................")
print("the python show TypeError: can only concatenate str (not int) to str ")
print(a+b)

#Part 8 — String Repetition
#Task 16
a="$^@"
print("Output for task 16:.................................................")
print(a*3)
print(a*5)
print(a*10)

#Task 17 — Pattern
a="*"
print("Output for task 17:.................................................")
print(a*10)

#Part 9 — Case Conversion
#Task 18
a="python programming language"
print("Output for task 18:.................................................")
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())

#Task 19 — Case-Insensitive Comparison
a="Python"
b="python"
print("Output for task 19:.................................................")
print(a==b)
print(a.lower()==b.lower())

#Part 10 — Searching
#Task 20 — Membership
a="Python is a programming language"
print("Output for task 20:.................................................")
print("Python" in a)
print("programming" in a)
print("Java" in a)
print("language" in a)

#Task 21 — find()
a="Python is a programming language"
print("Output for task 21:.................................................")
print(a.find("Python"))
print(a.find("programming"))
print(a.find("language"))
print(a.find("Java"))

#Task 22 — index()
a="Python is a programming language"
print("Output for task 22:.................................................")
print(a.index("Python"))
print(a.index("programming"))
print(a.index("language"))
print(""" when using this a.index("Java") python show ValueError: substring not found """)

#Task 23 — Count Characters
a="banana"
print("Output for task 23:.................................................")
print(a.count("a"))
print(a.count("n"))
print(a.count("b"))

#Task 24 — Starts and Ends
filename = "student_notes.pdf"
print("Output for task 24:.................................................")
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))

#Part 11 — Replacing
#Task 25 — Replace a Word
text = "I am learning Java"
text1=text.replace("Java","Python")
print("Output for task 25:.................................................")
print(text1)

#Task 26 — Multiple Replacements
text = "apple apple apple"
text1=text.replace("apple","mango")
print("Output for task 26:.................................................")
print(text1)

#Task 27 — Limited Replacement
text = "apple apple apple"
text1=text.replace("apple","mango",1)
print("Output for task 27:.................................................")
print(text1)

#Task 28 — Check Immutability
text = "Python"
text.upper()
print("Output for task 28:.................................................")
print(text ,"the original string not changed because not store value in variable")
text=text.upper()
print(text)

#Part 12 — Whitespace
#Task 29
text = "   Python Programming   "
print("Output for task 29:.................................................")
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Task 30 — User Input
user_input=input("Enter your name:")
print("Output for task 30:.................................................")
print(user_input.strip())

#Part 13 — Split and Join
#Task 31 — Split
string="Python is easy to learn"
print("Output for task 31:.................................................")
list=string.split()
print(list)

#Task 32 — Split with Separato
string="apple,banana,mango,orange"
print("Output for task 32:.................................................")
list=string.split(",")
print(list)

#Task 33 — Join
words = ["Python", "is", "easy"]
print("Output for task 33:.................................................")
result=" ".join(words)
print(result)

#Task 34 — Join with Different Separators
words=["Python","is","easy"]
print("Output for task 34:.................................................")
result="-".join(words)
print(result)
result="/".join(words)
print(result)

#Part 14 — String Formatting
#Task 35 — F-String
Name="Praveen Prajapati"
Age=18
City="Nagaur Rajasthan"
print("Output for task 35:.................................................")
sentence=f"My name is {Name} and I am {Age} years old and I am form {City}"
print(sentence)

#Task 36 — Arithmetic Inside F-String
a = 10
b = 20
print("Output for task 36:.................................................")
sum=f"{a+b}"
print(sum)

#Part 15 — Error Identification
#Task 37
print("Output for task 37:.................................................")
#A
text = "Python"
print("print(text[20]) this will show IndexError: string index out of range")
print(text[2])

#B
text = "Python"
print("text[0] = 'J' this will show TypeError: 'str' object does not support item assignment")
print(text[0])

#C
age = 20
print("print('Age: ' + age) this will show TypeError: can only concatenate str (not 'int') to str")
print("Age: " + str(age))

#D
text = "Python"
print("print(text.index('Java')) this will show ValueError: substring not found")
print(text.index("Python"))

#Part 16 — Practical Challenge
#Task 38 — Name Processor
print("Output for task 38:.................................................")
user_fullname=input("Enter your full name:")
cleaned_name=user_fullname.strip()
print(user_fullname)
print(cleaned_name)
print(user_fullname.upper())
print(user_fullname.lower())
print(user_fullname.title())
length=len(user_fullname)
print(length)
print(user_fullname[0])
print(user_fullname[length-1])
print("a" in user_fullname)

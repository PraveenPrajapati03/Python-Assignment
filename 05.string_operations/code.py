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
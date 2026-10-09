#1
choice=int(input("enter your choice:\n1=>Pizza\n2=>Burger\n3=>Pasta\n4=>Sandwich\n>>>"))
match choice:
    case 1:
        print("You selected Pizza")
    case 2:
        print("You selected Burger")
    case 3:
        print("You selected Pasta")
    case 4:
        print("You selected Sandwich")
    case _:
        print("Invalid Menu Choice")


#2
choice = int(input("Enter your choice (1-5):\n1=>Wi-Fi\n2=>Bluetooth\n3=>Mobile Data\n4=>Airplane Mode\n5=>Exit\n>>>> "))
match choice:
    case 1:
        print("Wi-Fi Selected")
    case 2:
        print("Bluetooth Selected")
    case 3:
        print("Mobile Data Selected")
    case 4:
        print("Airplane Mode Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")


#3
choice = int(input("Enter your choice (1-5):\n1=>Check Balance\n2=>Withdraw Money\n3=>Deposit Money\n4=>Change PIN\n5=>Exit\n>>>> "))
match choice:
    case 1:
        print("Check Balance Selected")
    case 2:
        print("Withdraw Money Selected")
    case 3:
        print("Deposit Money Selected")
    case 4:
        print("Change PIN Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")


#4
signal=int(input("enter the signal color choice:\n1=>Red\n2=>Yellow\n3=>Green\n>>>>"))
match signal:
    case 1:
        print("Stop")
    case 2:
        print("Wait")
    case 3:
        print("Go")
    case _:
        print("Invalid Signal")


#5
choice=int(input("enter your choice-\n1 → View Profile\n 2 → View \n 3 → View Marks\n 4 → View Attendance\n 5 → Logout\n>>>>>>"))
match choice:
    case 1:
        print("Opening profile")
    case 2:
        print("opening courses")
    case 3:
        print("opening marks")
    case 4:
        print("opening Attendance")
    case 5:
        print("logout")
    case _:
        print("invalid choice")


#6
choice=int(input("enter your choice-\n1 → Electronics\n 2 → Clothing \n 3 → Books\n 4 → Grocery\n 5 → Exit\n>>>>>>"))
match choice:
    case 1:
        print("Opening Electronics")
    case 2:
        print("opening Clothing")
    case 3:
        print("opening Books")
    case 4:
        print("opening Grocery")
    case 5:
        print("Exit")
    case _:
        print("invalid choice")


#7
choice=int(input("enter your choice-\n1 → Account Balance\n 2 → Mini Statement \n 3 → Fund Transfer\n 4 → Bill Payment\n 5 → Customer Support\n>>>>>>"))
match choice:
    case 1:
        print("Opening Account Balance")
    case 2:
        print("opening Mini Statement")
    case 3:
        print("opening Fund Transfer")
    case 4:
        print("opening Bill Payment")
    case 5:
        print("Customer Support")
    case _:
        print("invalid choice")

#8
choice=int(input("enter your choice-\n1 → Morning Show\n 2 → Afternoon Show \n 3 → Evening Show\n 4 → Night Show\n>>>>>>"))
match choice:
    case 1:
        print("Morning Show Selected")
    case 2:
        print("Afternoon Show Selected")
    case 3:
        print("Evening Show Selected")
    case 4:
        print("Night Show Selected")
    case _:
        print("invalid choice")


#9
choice=int(input("Enter weather:\n1 → sunny\n 2 → rainy \n 3 → cloudy\n 4 → Night Show\n>>>>>>"))
match choice:
    case 1:
        print("sunny  → Wear sunglasses")
    case 2:
        print("rainy  → Carry an umbrella")
    case 3:
        print("cloudy → Weather may change")
    case 4:
        print("snowy  → Wear warm clothes")
    case _:
        print("invalid Weather")


#10
choice=int(input("Enter payment method:\n1 → upi\n 2 → card \n 3 → case\n 4 → wallet\n>>>>>>"))
match choice:
    case 1:
        print("UPI Payment Selected")
    case 2:
        print("card Payment Selected")
    case 3:
        print("case Payment Selected")
    case 4:
        print("wallet Payment Selected")
    case _:
        print("invalid method")


#11
choice=int(input("Enter extension:\n1 → pdf\n 2 → jpg \n 3 → png\n 4 → mp3\n 5 → mp4\n>>>>>>"))
match choice:
    case 1:
        print("Document file")
    case 2:
        print("Image file")
    case 3:
        print("Image file")
    case 4:
        print("Audio file")
    case 5:
        print("Video file")
    case _:
        print("Unknown File Type")


#12
choice=int(input("Enter role:\n1 → admin\n 2 → teacher \n 3 → student\n 4 → guest\n >>>>>>"))
match choice:
    case 1:
        print("admin   → Full Access")
    case 2:
        print("teacher → Teacher Dashboard")
    case 3:
        print("student → Student Dashboard")
    case 4:
        print("guest   → Limited Access")
    case _:
        print("Invalid Role")


#13
choice=int(input("Enter day number:\n1 → Monday\n 2 → Tuesday \n 3 → Wednesday\n 4 → Thursday\n 5 → Friday\n 6 → Saturday\n 7 → Sunday\n>>>>>>"))
match choice:
    case 1 |2 |3 |4 | 5:
        print("Weekday")
    case 6 |7:
        print("Weekend")
    case _:
        print("Invalid Day")

#14
choice=int(input("Enter priority number:\n1 → Low\n 2 → Medium \n 3 → High\n 4 → Critical\n>>>>>>"))
match choice:
    case 1 |2 :
        print("Normal Priority")
    case 4 |5:
        print("Urgent Priority")
    case _:
        print("Invalid input")

#15
choice=int(input("Enter category number:\n1 → Bronze\n 2 → Silver \n 3 → Gold\n 4 → Platinum\n>>>>>>"))
match choice:
    case 1 |2 :
        print("Basic Membership")
    case 4 |5:
        print("Premium Membership")
    case _:
        print("Invalid category")


#Topic 5 — Nested match-case

#16
choice=int(input("Enter user type:\n1 → Student\n 2 → Teacher \n>>>>>>"))
match choice:
    case 1 :
        show=int(input("enter to show:\n1 → View Courses\n 2 → View Marks \n 3 → View Attendance \n>>>>>>"))
        match show:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student attendance")
            case  _:
                print("invalid input")
    case 2:
        show=int(input("enter to show:\n1 → View Students\n 2 → Enter Marks \n 3 → View Attendance \n>>>>>>"))
        match show:
            case 1:
                print("Opening Student data")
            case 2:
                print("enter Student Marks")
            case 3:
                print("viwe Student attendance")
            case  _:
                print("invalid input")
    case _:
        print("invaid user type")


#17
choice=int(input("Enter account type:\n1 → Savings\n 2 → Current \n>>>>>>"))
match choice:
    case 1 :
        show=int(input("Enter operation:\n1 → Check Balance\n 2 → Deposit \n 3 → Withdraw \n>>>>>>"))
        match show:
            case 1:
                print("Savings Account\n Check Balance Selected")
            case 2:
                print("Savings Account\n Deposit Selected")
            case 3:
                print("Savings Account\n Withdraw Selected")
            case  _:
                print("invalid operation")
    case 2 :
        show=int(input("Enter operation:\n1 → Check Balance\n 2 → Deposit \n 3 → Withdraw \n>>>>>>"))
        match show:
            case 1:
                print("Current Account\n Check Balance Selected")
            case 2:
                print("SaviCurrentngs Account\n Deposit Selected")
            case 3:
                print("SavinCurrentgs Account\n Withdraw Selected")
            case  _:
                print("invalid operation")
    case _:
        print("invalid account type")


#18
choice=int(input("Enter category:\n1 → Electronics\n 2 → Clothing \n>>>>>>"))
match choice:
    case 1 :
        show=int(input("Enter product:\n1 → Mobile\n 2 → Laptop \n 3 → Headphones \n>>>>>>"))
        match show:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case  _:
                print("invalid product")
    case 2 :
        show=int(input("Enter product:\n1 → Shirt\n 2 → Jeans \n 3 → Shoes \n>>>>>>"))
        match show:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case  _:
                print("invalid product")
    case _:
        print("invalid catagory")


#19
choice=int(input("Enter category:\n1 → Vegetarian\n 2 → Non-Vegetarian \n>>>>>>"))
match choice:
    case 1 :
        show=int(input("Enter food:\n1 → Paneer\n 2 → Dal \n 3 → Veg Biryani \n>>>>>>"))
        match show:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case  _:
                print("invalid food")
    case 2 :
        show=int(input("Enter food:\n1 → Chicken Biryani\n 2 → Chicken Curry \n 3 → Fish Fry \n>>>>>>"))
        match show:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case  _:
                print("invalid food")
    case _:
        print("invalid catagory")


#20
choice=int(input("Enter operator:\n1 → +\n 2 → -\n 3 → *\n 4 → /\n>>>>>>"))
num1=float(input("enter the first number:-"))
num2=float(input("enter the second number:-"))
match choice:
    case 1 :
        print(f"Addition of {num1} and {num2} is {num1+num2}")
    case 2 :
        print(f"Subtraction of {num1} and {num2} is {num1-num2}")
    case 3 :
        print(f"Multiplication of {num1} and {num2} is {num1*num2}")
    case 4 :
        if num2==0:
            print("zero division error enter an valid number:")
        else:
            print(f"Division of {num1} and {num2} is {num1/num2}")
    case _:
        print("invalid Operator")


#21
choice=int(input("Enter converter:\n1 → Celsius to Fahrenheit\n 2 → Fahrenheit to Celsius\n >>>>>>"))
temp=float(input("enter the temperature:-"))
match choice:
    case 1:
        ftemp=(temp*(9/5))+32
        print("The temperature in fahrenheit is",ftemp,"°F")
    case 2:
        ctemp=(temp-32)*(5/9)
        print("The temperature in calsius is",ctemp,"°C")
    case _:
        print("invalid Input")


#22
choice=int(input("Enter choice:\n1 → Kilometers to Meters\n 2 → Meters to Kilometers\n 3 → Kilograms to Gramss\n 4 → Grams to Kilograms\n >>>>>>"))
value=float(input("Enter value:-"))
match choice:
    case 1:
        meter=value*1000
        print("The distance in meter  is",meter,"m")
    case 2:
        km=value/1000
        print("The distance in km  is",km,"km")
    case 3:
        gram=value*1000
        print("The weight in gram  is",gram,"g")
    case 4:
        kg=value/1000
        print("The weight  in kg is",kg,"kg")
    case _:
        print("invalid Input")


#23
choice=int(input("Enter account type:\n1 → Savings\n 2 → Current \n>>>>>>"))
match choice:
    case 1 :
        show=int(input("Enter operation:\n1 → Check Balance\n 2 → Deposit \n 3 → Withdraw \n>>>>>>"))
        match show:
            case 1:
                print("Savings Account\n Check Balance Selected")
            case 2:
                print("Savings Account\n Deposit Selected")
            case 3:
                amount=int(input("enter the amount to withdrawl"))
                if amount>0:
                    print("Savings Account\n Withdrawal Request Accepted")
                else:
                    print("Invalid amount")               
            case  _:
                print("invalid operation")
    case 2 :
        show=int(input("Enter operation:\n1 → Check Balance\n 2 → Deposit \n 3 → Withdraw \n>>>>>>"))
        match show:
            case 1:
                print("Current Account\n Check Balance Selected")
            case 2:
                print("SaviCurrentngs Account\n Deposit Selected")
            case 3:
                amount=int(input("enter the amount to withdrawl"))
                if amount>0:
                    print("Current Account\n Withdrawal Request Accepted")
                else:
                    print("Invalid amount") 
            case  _:
                print("invalid operation")
    case _:
        print("invalid account type")


#24
menu=int(input("Enter your choice:\n1 → Start Exam\n 2 → View Result \n 3 → Exit \n>>>>>>"))
match menu:
    case 1:
        age=int(input("enter your age:-"))
        if age>=18:
            print("You can start the exam")
        else:
            print("not allowed to start exam")
    case _:
        print("invalid choice")


#25
menu=int(input("Enter your choice:\n1 → Regular\n 2 → Premium \n 3 → VIP \n>>>>>>"))
match menu:
    case 1:
        age=int(input("enter your age:-"))
        if age<=5:
            print("Free Entry")
        else:
            print("regular")
    case 2:
        age=int(input("enter your age:-"))
        if age<=5:
            print("Free Entry")
        else:
            print("Primium")
    case 3:
        age=int(input("enter your age:-"))
        if age<=5:
            print("Free Entry")
        else:
            print("VIP")
    case _:
        print("invalid choice")


#26
choice=int(input("Enter device:\n1 → Light\n 2 → Fan \n 3 → AC\n 4 → TV\n>>>>>>"))
match choice:
    case 1:
        print("Light Controller Opened")
    case 2:
        print("Fan Controller Opened")
    case 3:
        print("AC Controller Opened")
    case 4:
        print("TV Controller Opened")
    case _:
        print("invalid device")


#27
choice=int(input("Enter device:\n1 → General Medicine\n 2 → Cardiology \n 3 → Orthopedics\n 4 → Pediatrics\n 5 → Emergency\n>>>>>>"))
match choice:
    case 1:
        print("General Medicine department")
    case 2:
        print("Cardiology department")
    case 3:
        print("Orthopedics department")
    case 4:
        print("Pediatrics department")
    case 5:
        print("Emergency department")
    case _:
        print("invalid department")


#28
choice=int(input("Enter railway service:\n1 → Book Ticket\n2 → Cancel Ticket\n3 → Check PNR\n4 → Train Schedule\n5 → Exit\n>>>>>>"))
match choice:
    case 1:
        print("Book Ticket")
    case 2:
        print("Cancel Ticket")
    case 3:
        print("Check PNR")
    case 4:
        print("Train Schedule")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")


#29
choice=int(input("Enter library service:\n1 → Search Book\n2 → Issue Book\n3 → Return Book\n4 → View Issued Books\n5 → Exit\n>>>>>>"))
match choice:
    case 1:
        print("Search Book")
    case 2:
        print("Issue Book")
    case 3:
        print("Return Book")
    case 4:
        print("View Issued Books")
    case 5:
        print("Exit")
    case _:
        print("Invalid choice")


#30
status=input("Enter order status:\nplaced\nconfirmed\npreparing\nout_for_delivery\ndelivered\ncancelled\n>>>>>>").lower().strip()
match status:
    case "placed":
        print("Your order has been placed")
    case "confirmed":
        print("Your order has been confirmed")
    case "preparing":
        print("Your order is being prepared")
    case "out_for_delivery":
        print("Your order is on the way")
    case "delivered":
        print("Your order has been delivered")
    case "cancelled":
        print("Your order has been cancelled")
    case _:
        print("Invalid order status")


#31
banking_type = int(input("Enter banking type: "))
banking_option = int(input("Enter option: "))
match banking_type:
    case 1:
        match banking_option:
            case 1:
                print("Personal Balance Selected")
            case 2:
                print("Personal Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")
    case 2:
        match banking_option:
            case 1:
                print("Business Balance Selected")
            case 2:
                print("Business Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")
    case _:
        print('Invalid Banking Type')


#32
user_type = int(input("Enter user type: "))
user_option = int(input("Enter option: "))
match user_type:
    case 1:
        match user_option:
            case 1:
                print("Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Homework Selected")
            case _:
                print("Invalid Option")
    case 2:
        match user_option:
            case 1:
                print("Enter Marks Selected")
            case 2:
                print("Attendance Selected")
            case 3:
                print("Assign Homework Selected")
            case _:
                print("Invalid Option")
    case 3:
        match user_option:
            case 1:
                print("Child Marks Selected")
            case 2:
                print("Child Attendance Selected")
            case 3:
                print("Contact Teacher Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid User")


#33
transport = int(input("Enter transport: "))
travel_option = int(input("Enter option: "))
match transport:
    case 1:
        match travel_option:
            case 1:
                print("Economy Flight Selected")
            case 2:
                print("Business Flight Selected")
            case _:
                print("Invalid Option")
    case 2:
        match travel_option:
            case 1:
                print("Sleeper Train Selected")
            case 2:
                print("AC Train Selected")
            case _:
                print("Invalid Option")
    case 3:
        match travel_option:
            case 1:
                print("Ordinary Bus Selected")
            case 2:
                print("Volvo Bus Selected")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid transport.")


#34
option = int(input("Enter option from \n1 → Start Game\n2 → Load Game\n3 → Settings\n4 → Exit\n======>"))
match option:
    case 1:
        print("Start Game")
    case 2:
        print("Load Game")
    case 3:
        choice = int(input("Enter Choice: "))

        match choice:
            case 1:
                print("Sound")
            case 2:
                print("Graphics")
            case 3:
                print("Controls")
            case _:
                print("Invalid option")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")


#35
category = int(input("Enter category: "))
match category:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Soup")
            case 2:
                print("Spring Roll")
            case 3:
                print("Garlic Bread")
            case _:
                print("Invalid Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Pizza")
            case 2:
                print("Pasta")
            case 3:
                print("Biryani")
            case _:
                print("Invalid Option")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Ice Cream")
            case 2:
                print("Cake")
            case 3:
                print("Gulab jamun")
            case _:
                print("Invalid Option")
    case 4:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Coffee")
            case 2:
                print("Tea")
            case 3:
                print("Juice")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Category")


#36
payment_type = int(input("Enter Payment Type: "))
match payment_type:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Scan QR")
            case 2:
                print("Enter UPI ID")
            case _:
                print("Invalid Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Credit Card")
            case 2:
                print("Deit Card")
            case _:
                print("Invalid Option")
    case 3:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Add Money")
            case 2:
                print("Pay Using Wallet")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid method")


#37
category = int(input("Enter category: "))
option = int(input("Enter option: "))
match category:
    case 1:
        match option:
            case 1:
                print("Python")
            case 2:
                print("Java")
            case 3:
                print("C++")
            case _:
                print("Invalid option")
    case 2:
        match option:
            case 1:
                print("Algebra")
            case 2:
                print("Calculus")
            case 3:
                print("Statistics")
            case _:
                print("Invalid option")
    case 3:
        match option:
            case 1:
                print("English")
            case 2:
                print("Presentation")
            case 3:
                print("Interview Skills")
            case _:
                print("Invalid option")
    case _:
        print("Invalid category")


#38
category = int(input("Enter category: "))
option = int(input("Enter option: "))
match category:
    case 1:
        match option:
            case 1:
                print("Start")
            case 2:
                print("Stop")
            case _:
                print("Invalid Option")
    case 2:
        match option:
            case 1:
                print("Headlights")
            case 2:
                print("Indicators")
            case 3:
                print("Hazard Lights")
            case _:
                print("Invalid Option")
    case 3:
        match option:
            case 1:
                print("Play")
            case 2:
                print("Pause")
            case 3:
                print("Next")
            case 4:
                print("Previous")
            case _:
                print("Invalid Option")
    case 4:
        match option:
            case 1:
                print("Start Navigation")
            case 2:
                print("Stop Navigation")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Category")


#39
role = input("Enter role: ")
option = int(input("Enter option: "))
match role:
    case 1:
        match option:
            case 1:
                print("View Profile")
            case 2:
                leave_days = int(input("Enter number of days for leave: "))
                if leave_days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3:
                print("View Salary")
            case _:
                print("Invalid option")
    case 2:
        match option:
            case 1:
                print("View Team")
            case 2:
                print("Approve Team")
            case 3:
                print("View Reports")
            case _:
                print("Invalid option")
    case _:
        print("Invalid role")


#40
role = int(input("Enter role: "))
option = int(input("Enter option: "))
match role:
    case 1:
        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Option")
    case 2:
        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Option")
    case 3:
        match option:
            case 1:
                print("Opening Administration Fees")
            case 2:
                print("Opening Administration Admission")
            case 3:
                print("Opening Administration Notices")
            case 4:
                print("Opening Administration Departments")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid Role")
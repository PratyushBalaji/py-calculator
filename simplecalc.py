#Operation Selection
print("Welcome to the simple python calculator")
print("Type 'exit' or 'quit' to close the program")
print()
print("What operation would you like to perform?")
print()
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print()

def calculate():

    #input to type selection
    x = input("")

    #Addition code
    if x == '1':
        print()
        print("You have chosen Addition (Option 1)")
        print()
        y = int(input("What is the 1st number? "))
        z = int(input("What is the 2nd number? "))
        total = y + z
        print()
        print(y,"+",z,"=",total,"!")
        print()
        choice = input("Would you like to calculate another number? : ")
        if choice.lower() == "n":
            print("Thanks for using calculator!")
            input()
            quit()
        elif choice.lower() == 'y':
            print("Choose 1(+), 2(-), 3(×), 4(÷) or exit")
            calculate()

    #Subtraction code
    if x == '2':
        print()
        print("You have chosen Subtraction (Option 2)")
        print()
        y = int(input("What is the 1st number? "))
        z = int(input("What is the 2nd number? "))
        total = y - z
        print()
        print(y,"-",z,"=",total,"!")
        print()
        choice = input("Would you like to calculate another number? : ")
        if choice.lower() == "n":
            print("Thanks for using calculator!")
            input()
            quit()
        elif choice.lower() == 'y':
            print("Choose 1(+), 2(-), 3(×), 4(÷) or exit")
            calculate()

    #Multiplication code
    if x == '3':
        print()
        print("You have chosen Multiplication (Option 3)")
        print()
        y = int(input("What is the 1st number? "))
        z = int(input("What is the 2nd number? "))
        total = y * z
        print()
        print(y,"×",z,"=",total,"!")
        print()
        choice = input("Would you like to calculate another number? : ")
        if choice.lower() == "n":
            print("Thanks for using calculator!")
            input()
            quit()
        elif choice.lower() == 'y':
            print("Choose 1(+), 2(-), 3(×), 4(÷) or exit")
            calculate()

    #Division code    
    if x == '4':
        print()
        print("You have chosen Division (Option 4)")
        print()
        y = int(input("What is the 1st number? "))
        z = int(input("What is the 2nd number? "))
        total = y / z
        print()
        print(y,"÷",z,"=",total,"!")
        print()
        choice = input("Would you like to calculate another number? : ")
        if choice.lower() == "n":
            print("Thanks for using calculator!")
            input()
            quit()
        elif choice.lower() == 'y':
            print("Choose 1(+), 2(-), 3(×), 4(÷) or exit")
            calculate()

    #Exit code
    if x.lower() == 'exit' or x.lower() == 'quit':
        quit()

calculate()
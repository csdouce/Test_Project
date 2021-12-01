# Intro to Python - Lesson 18 Exercise 1
# Program to practice using functions
# Chris Doucette
# Completed October 27, 2021

# Constants

# Functions created
def CelcToFahr():
    #1. Convert Celsius to Fahrenheit.
    print()
    Celsius = float(input("Enter a Celsius temperature to be converted to Fahrenheit."))

    # Converting input to Fahrenheit
    Fahrenheit = 9/5 * Celsius + 32
    print()
    print(f"Temperature in Celsius      {Celsius}")
    print(f"Temperature in Fahrenheit:  {Fahrenheit}")
    print()
    AnyKey = input("Press any key to continue...")

def CalcPlatoWife():
    # 2. Plato's Ideal Wife.
    print()
    Age = int(input("Enter the age of the man: "))

    # Calculating wife's ideal age
    IdealAge = int(Age / 2 + 7)

    #Print desired output
    print()
    print(f"Man's age:        {Age}")
    print(f"Wife's ideal age: {IdealAge}")
    print()
    AnyKey = input("Press any key to continue...")

def DeterTrainHR():
    # 3. Determine Training Heart Rate.
    print()
    Age = int(input("Enter your age: "))
    RestHR = int(input("Enter your resting hear rate: "))

    # Calculatings to find training hear rate
    TrainingHR = 220 - Age
    TrainingHR -= RestHR
    TrainingHR = TrainingHR * .6
    TrainingHR += RestHR

    # Printing the Training Heart Rate
    print()
    print(f"Your age is:                 {Age}")
    print(f"Your resting heart is:       {RestHR}")
    print(f"Your training heart rate is: {TrainingHR}")
    print()
    AnyKey = input("Press any key to continue...")

def DaysToChrismas():
    # 4. How many days to Christmas.
    import datetime

    # Getting todays date
    TodayDate = datetime.datetime.now()

    #Contstruction Christmas date
    if TodayDate.month == 12 and TodayDate.day >= 25:
        ChristmasYear = str(TodayDate.year+1)
        ChristmasDate = f"12-25-{ChristmasYear}"
        ChristmasDate = datetime.datetime.strptime(ChristmasDate, "%m-%d-%Y")
    else:
        ChristmasYear = str(TodayDate.year)
        ChristmasDate = f"12-25-{ChristmasYear}"
        ChristmasDate = datetime.datetime.strptime(ChristmasDate, "%m-%d-%Y")

    # Calculating the number of days until Christmas
    NumDays = ChristmasDate - TodayDate

    # printing the required results
    print()
    print(f"Today's date is:                    {TodayDate.strftime('%A %B %-d, %Y')}")
    print(f"Number of days until Christmas:     {NumDays.days} days")
    print()
    AnyKey = input("Press any key to continue...")

def FindLetGrade():
    # 5. Find a Letter Grade
    print()
    GradeNum = int(input("Enter your grade: "))

    if GradeNum >= 80:
        GradeAlpha = "A"
    elif GradeNum >= 70:
        GradeAlpha = "B"
    elif GradeNum >= 60:
        GradeAlpha = "C"
    elif GradeNum >= 50:
        GradeAlpha = "D"
    else:
        GradeAlpha = "F"

    print()
    print(f"Numeric grade is:       {GradeNum}")
    print(f"Alpha grade is:         {GradeAlpha}")
    print()
    AnyKey = input("Press any key to continue...")

def HowOldInvoice():
    # 6. How old is an invoice.
    import datetime

    print()
    # User inputs
    CompName = input("Enter the Company Name: ")
    while True:
        InvoiceDate = input("Enter the invoice date (YYYY-MM-DD): ")

        InvoiceDate = datetime.datetime.strptime(InvoiceDate, "%Y-%m-%d")

        if InvoiceDate > datetime.datetime.now():
            print("Input error. Invoice date cannot be greater than today's date. ")
        else:
            break

    while True:
        try:
            InvoiceAmt = float(input("Enter the invoice amount: "))
        except:
            print("Invalid input. Please enter the invoice amount.")
        else:
            break

    #Checking to see how old the invoice is
    TodaysDate = datetime.datetime.now()
    NumDays = TodaysDate.date() - InvoiceDate.date()

    # Criteria on what to print depending on how many days old reciept is
    print()
    if NumDays.days <= 30:
        print("OK")
    elif NumDays.days >= 31 and NumDays.days <= 60:
        print("Better think about paying.")
    elif NumDays.days > 60:
        print("This one could be in trouble.")

    print()
    AnyKey = input("Press any key to continue...")

def GuessGame():
    # 7. Play my guessing game
    print()

    import random

    RandNum = random.randrange(1,100)
    Count = 0

    while True:
        try:
            Guess = int(input("Guess a number between 1 and 100: "))
        except:
            print("Input error. Pick a number between 1 and 100.")
        else:
            if Guess < 1 and Guess > 100:
                print("Input error. You're number was not between 1 and 100 - please re-enter.")
            else:
                if RandNum != Guess:
                    if RandNum < Guess:
                        print("Random Number was lower than your guess. Please take another guess between 1 and 100.")
                        print()
                    elif RandNum > Guess:
                        print("Random Number was higher than your guess. Please take another guess between 1 and 100.")
                        print()
                    Count += 1
                else:
                    print()
                    print(f"Congrats you picked the correct number ({Guess}) in {Count} guesses.")
                    print()
                    AnyKey = input("Press any key to continue...")
                    break

# Main program
while True:
    print()
    print("Mo's Quick Problems - Main Menu")
    print()
    print("1. Convert Celesius to Fahrenheit.")
    print("2. Plato's Ideal Wife.")
    print("3. Determine Training Heart Rate.")
    print("4. How many days to Christmas.")
    print("5. Find a Letter Grade.")
    print("6. How old is an invoice.")
    print("7. Play my guessing game.")
    print("8. Quit.")
    print()
    while True:
        try:
            Choice = int(input("   Enter Choice(1-8): "))
        except:
            print("Invalid input - you must enter 1-8 for you selection.")
        else:
            if Choice <1 or Choice > 8:
                print("Invalid input. Must be between 1 and 8")
            else:
                break

    if Choice == 1:
        CelcToFahr()
    elif Choice == 2:
        CalcPlatoWife()
    elif Choice == 3:
        DeterTrainHR()
    elif Choice == 4:
        DaysToChrismas()
    elif Choice == 5:
        FindLetGrade()
    elif Choice == 6:
        HowOldInvoice()
    elif Choice == 7:
        GuessGame()
    else:
        exit()




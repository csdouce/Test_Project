# Intro to Python - Lesson 23 Exercise 1
# Updating Modern Movie Rentals to read Constants from file
# Chris Doucette
# Completed November 4, 2021
import datetime
import time

# Reading constants from file
f = open('../../../../Intro to Python/Lesson 23/L23E1/Def.dat', 'r')
MOVIE_ID = int(f.readline())
HST_RATE = float(f.readline())
NUM_DAYS_NEW_RELEASE = int(f.readline())
WEEKS_REMOVE_SHELF = int(f.readline())
f.close()

while True:

    MovieName = input("Enter the movie name (END to delete): ")

    # Exit program on user command
    if MovieName.upper() == "END":
        break

    while True:
        ReleaseDate = input("Enter the release date of movie (YYYY-MM-DD): ")

        # Change date string to date object
        try:
            ReleaseDate = datetime.datetime.strptime(ReleaseDate, "%Y-%m-%d")
        except:
            print("Invalid input. Release date must be in the format YYYY-MM-DD - Please re-enter.")
        else:
            break

    MovieType = input("Enter the movie type (D, C, M or H): ").upper()
    MovieRating = input("Enter the movie rating (G, P, R): ").upper()
    RentalCost = float(input("Enter the rental cost: "))

    # Calculating the taxes and total rental costs including tax
    HstPaid = RentalCost * HST_RATE
    TotRentCost = RentalCost + HstPaid

    NewReleaseEndDate = ReleaseDate + datetime.timedelta(days=NUM_DAYS_NEW_RELEASE)
    RemoveShelfDate = ReleaseDate + datetime.timedelta(weeks=WEEKS_REMOVE_SHELF)

    # Printing out calculated results
    print()
    print(f"HST Paid:               ${HstPaid:,.2f}")
    print(f"Total Rental Cost:      ${TotRentCost:,.2f}")
    print(f"New Release End Date:   {NewReleaseEndDate.date()}")
    print(f"Remove from Shelf Date: {RemoveShelfDate.date()}")
    print()

    # Writing information to Movies.dat file
    f = open("../../../../Intro to Python/Lesson 23/L23E1/Movies.dat", "a")
    f.write(f"{str(MOVIE_ID)}, ")
    f.write(f"{str(ReleaseDate)}, ")
    f.write(f"{MovieName}, ")
    f.write(f"{MovieType}, ")
    f.write(f"{MovieRating}, ")
    f.write(f"{str(RentalCost)}, ")
    f.write(f"{str(HstPaid)}, ")
    f.write(f"{str(TotRentCost)}, ")
    f.write(f"{str(NewReleaseEndDate.date())}, ")
    f.write(f"{str(RemoveShelfDate.date())}\n")
    f.close()

    # Updating move id for next movie addition
    MOVIE_ID += 1

    # Displaying saving message
    print("Saving... ", end="")
    for wait in range(1,11):
        print("*", end="")
        time.sleep(.5)
    print(f" ...Movie information for {MovieName} successfully saved.")
    print()

    anykey = input("Press any key to continue")
    print()

# Writing Defaults back to file and close file
f = open('../../../../Intro to Python/Lesson 23/L23E1/Def.dat', 'w')
f.write(f"{str(MOVIE_ID)}\n")
f.write(f"{str(HST_RATE)}\n")
f.write(f"{str(NUM_DAYS_NEW_RELEASE)}\n")
f.write(f"{str(WEEKS_REMOVE_SHELF)}\n")
f.close()
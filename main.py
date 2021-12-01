# Intro to Python - Lesson 28 Exercise 1
# Creating functions that deal with lists
# Chris Doucette
# Completed November 29, 2021

# Functions
def display_list(my_list):
    # Function that prints all items from a list with numbers in front of item
    count = 1
    print()
    for item in my_list:
        print(f"{count}. {item}")
        count += 1


def add_to_list(my_list):
    # Function to add to a list
    print()
    to_add = input("What do you want to add to the list? ")

    my_list.append(to_add)

    return my_list


def delete_from_list(my_list):
    # Function to delete an item from a list based on user feedback
    display_list(my_list)

    print()
    to_delete = int(input("Enter the number of the list item you want to delete. "))

    my_list.pop(to_delete - 1)

    return my_list


# Declaring list
DisplayList = ["Buy Maurice a tea", "Study Essentials", "Write a Python program"]

# Main menu of program
while True:
    print()
    print("Mo's TODO List - Main Menu")
    print()
    print("1. Display list.")
    print("2. Add item to list.")
    print("3. Delete item from list.")
    print("4. Quit.")
    print()

    while True:
        try:
            Choice = int(input("    Enter choice (1-4): "))
        except:
            print("You must enter a number between 1 and 4 - Please re-enter.")
        else:
            if Choice < 1 or Choice > 4:
                print("You must enter a number between 1 and 4 - Please re-enter.")
            else:
                break

    if Choice == 1:
        display_list(DisplayList)
        print()
        AnyKey = input("Press any key to continue")
    elif Choice == 2:
        DisplayList = add_to_list(DisplayList)
        print()
        AnyKey = input("Press any key to continue")
    elif Choice == 3:
        DisplayList = delete_from_list(DisplayList)
        print()
        AnyKey = input("Press any key to continue")
    elif Choice == 4:
        quit()
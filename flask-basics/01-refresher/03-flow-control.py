""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

# Loops
print("--------------------------")
print("IF Statements")
print("--------------------------")
may_continue = True
must_continue = 13

if may_continue:
    print("You may continue")
if must_continue == 13:
    print("You must continue")
if may_continue and must_continue == 13:
    print("You may and must continue")


# IF/ELSE
print("--------------------------")
print("IF/ELSE Statement")
print("--------------------------")
known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in known_people:
    print(f"I know {person}!")
else:
    print(f"I don't know {person}.")

# CODING EXERCISE
print("--------------------------")
print("CODING EXERCISE")
print("--------------------------")

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    """Returns even numbers"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

# Modify the below method so that "Quit" is returned if the choice parameter is "q".
def user_menu(choice):
    """Returns 'Quit' if choice is 'q'"""
    if choice == "a":
        return "Add"
    elif choice == 'q':
        return "Quit"
    return "Not a proper choice"

print(even_numbers())
print(user_menu('a'))
print(user_menu('q'))


# # BEFORE LIST COMPREHENSION
# def who_do_you_know():
#     """Ask user who they know and convert that string to a list"""
#     people = input("\nGive me a list of people you know, separated by commas\n")
#     people_list = people.split(",")

#     people_without_spaces = []
#     for p in people_list:
#         people_without_spaces.append(p.strip())

#     return people_without_spaces

# USING LIST COMPREHENSION
def who_do_you_know():
    """Ask user who they know and convert that string to a list"""
    people = input("\nGive me a list of people you know, separated by commas\n")
    people_list = people.split(",")

    people_without_spaces = [p.strip() for p in people_list]

    return people_without_spaces

print(who_do_you_know())

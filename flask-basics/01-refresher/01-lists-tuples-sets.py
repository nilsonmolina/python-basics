""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

# Lists, Tuples, and Sets
print("--------------------------")
print("List, Tuples, and Sets")
print("--------------------------")
list_of_grades = [90, 77, 80, 90]
tuple_of_grades = (90, 77, 80, 90)
set_of_grades = {90, 77, 80, 90}

print("List: ", list_of_grades)
print(" - Ordered and Mutable (can be changed)\n")

print("Tuple:", tuple_of_grades)
print(" - Ordered and Immutable (cannot be changed)\n")

print("Set:  ", set_of_grades)
print(" - Unordered, Immutable and Unique (90 may not be first value and is not doubled)\n")

# Operations for Lists, Tuples, and Sets
print("\nOperations for Lists, Tuples, and Sets")
print("--------------------------")
print("List:", list_of_grades)
print(" - len(list_of_grades):       ", len(list_of_grades))
print(" - sum(list_of_grades):       ", sum(list_of_grades))
print(" - list_of_grades[0]:         ", list_of_grades[0])
list_of_grades[0] = 60
print(" - list_of_grades[0] = 60:    ", list_of_grades)
list_of_grades.append(100)
print(" - list_of_grades.append(100):", list_of_grades)

print("\nTuple:", tuple_of_grades)
print(" - len(tuple_of_grades):       ", len(tuple_of_grades))
print(" - sum(tuple_of_grades):       ", sum(tuple_of_grades))
print(" - tuple_of_grades[0]:         ", tuple_of_grades[0])
print(" - tuple_of_grades[0] = 60:    ", "Traceback: 'tuple' does not support item assignment")
print(" - tuple_of_grades.append(100):", "Traceback: 'tuple' object has no attribute 'append'")
print("   * a workaround for appending a tuple is to redefine its value as shown below")
tuple_of_grades = tuple_of_grades + (100,)
print("     - tuple_of_grades = tuple_of_grades + (100,):", tuple_of_grades)

print("\nSet:", set_of_grades)
print(" - len(set_of_grades):       ", len(set_of_grades))
print(" - sum(set_of_grades):       ", sum(set_of_grades))
print(" - set_of_grades[0]:         ", "Traceback: 'set' object does not support indexing")
print(" - set_of_grades[0] = 60:    ", "Traceback: 'set' object does not support indexing")
print(" - set_of_grades.append(100):", "Traceback: 'set' object has no attribute 'append'")
print("   * a workaround for appending a set is to use the 'add' method as shown below")
set_of_grades.add(100)
print("     - set_of_grades.add(100):", set_of_grades)

# Advanced Set Operations
print("\nAdvanced Set Operations")
print("--------------------------")
print("INTERSECTION")
print("  EXERCISE: Using a set, find which of your lottery numbers matched the winning numbers.")
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}
print("\n  GIVEN:")
print("    your_lottery_numbers = ", your_lottery_numbers)
print("    winning_numbers =      ", winning_numbers)
print("\n  ANSWER:")
answer = your_lottery_numbers.intersection(winning_numbers)
# answer = winning_numbers.intersection(your_lottery_numbers) # same result
print("    your_lottery_numbers.intersection(winning_numbers)")
print(f"    {answer}")

print("\n\nUNION")
print("  EXERCISE: How many values will a union of the two given sets have? Solve in your head.")
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 3, 5, 7, 9, 11}
print("\n  GIVEN:")
print("    set_1 = ", set_1)
print("    set_2 = ", set_2)
print("\n  ANSWER:")
union = set_1.union(set_2)
# union = set_2.union(set_1) # same result
answer = len(union)
print("    union = set_1.union(set_2)")
print("    len(union)")
print(f"    {answer} - {union}")

print("\n\nDIFFERENCE")
print("  EXERCISE: How many values will a difference of the two given sets have?")
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 3, 5, 7, 9, 11}
print("\n  GIVEN:")
print("    set_1 = ", set_1)
print("    set_2 = ", set_2)
print("\n  ANSWER:")
difference = set_1.difference(set_2)
answer = len(difference)
print("    difference = set_1.difference(set_2)")
print("    len(difference)")
print(f"    {answer} - {difference}")
print("      OR")
difference = set_2.difference(set_1)
answer = len(difference)
print("    difference = set_2.difference(set_1)")
print("    len(difference)")
print(f"    {answer} - {difference}")

# CODING EXERCISE
print("\nCODING EXERCISES")
print("--------------------------")
print("1. Create a tuple, called 'my_tuple', with a single value in it.")
print("\nANSWER:")
print("  my_tuple = (100,)")
print("    OR")
print("  my_tuple = 100,")

""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

# Loops
print("--------------------------")
print("Loops: Intro")
print("--------------------------")
my_string = "hello"
print("my_string = 'hello'")
print("\n- We can access each letter of our string:")
print("  my_string[0] = ", my_string[0])
print("  my_string[1] = ", my_string[1])
print("  my_string[2] = ", my_string[2])
print("  my_string[3] = ", my_string[3])
print("  my_string[4] = ", my_string[4])
print("\n* But clearly this is not effective, as we need to repeat a lot of code.")

print("\n--------------------------")
print("For-In Loops")
print("--------------------------")
print("The 'for-in' loop works on iterables like strings, lists, sets, tuples and more...")
print(f"""
EXERCISE:
-------
create a string and print each letter.

CODE:
-------
my_string = 'hello'
for character in my_string:
    print(character)

OUTPUT:
-------""")
for character in my_string:
    print(character)

print(f"""
EXERCISE:
-------
create a list of numbers and print its square.

CODE:
-------
my_list = [1, 3, 5, 7, 9]
for number in my_list:
    print(number ** 2)

OUTPUT:
-------""")
my_list = [1, 3, 5, 7, 9]
for number in my_list:
    print(number ** 2)

print("\n--------------------------")
print("While Loops")
print("--------------------------")
print("The loop will continue only if the statement evaluates to true")

user_wants_number = True
while user_wants_number:
    print(10)

    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False

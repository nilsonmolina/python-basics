# name = input("Please enter your name: ")
# age = int(input("How old are you, {0} ".format(name)))
#
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("Please come back in {0} years.".format(18 - age))


# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher: ")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower: ")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time!")


# # --------------------- Part 2 -------------------------
# age = int(input("How old are you? "))

# # ---- AND operator - Both must be true - Python will continue checking until the first 'false' is found
# if age >= 16 and age <= 65:
# if (age >= 16) and (age <= 65):
# if 16 <= age <= 65:
#     print("Have a good day at work")

# # ---- OR operator - At least one must be true - Python will continue checking until the first 'true' is found
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# # ---- BOOLEAN values
# x = "false"
# if x:
#     print("x is true")
#
# print("""False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty  string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# # ---- not operator - reverses boolean
# print(not False)
# print(not True)
#
# age = int(input("How old are you: "))
#
# if not(age < 18):
#     print("You are old enough to vote!")
# else:
#     print("Please come back in {0} years.".format(18 - age))


parrot = "Norwegian Blue"

letter = input("Enter a letter: ")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me a {}, Bob".format(letter))

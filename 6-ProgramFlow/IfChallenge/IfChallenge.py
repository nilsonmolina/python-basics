# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# at least 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.


# # ---- MY SOLUTION
# name = input("Welcome to the Challenge!\nPlease enter your first name to continue: ")
# age = int(input("Hello {0}, can you please enter your age: ".format(name)))
#
# if (age >= 18) and (age <= 30):
#     print("We hope you enjoyed this challenge {}, please enjoy your holiday!".format(name))
# else:
#     print("It seems we must refuse your entry. Please direct all complaints to the challenge admin.")
#


# # ---- INSTRUCTOR SOLUTION
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
#
# # if age >=18 and age <31:
# if 18 <= age < 31:
#     print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#     print("I'm sorry, our holidays are only for seriously cool people")

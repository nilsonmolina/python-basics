# for i in range(10):
#     print("i is now {0}".format(i))
#
# i = 0
# while i < 10:
#     print("i is now {0}".format(i))
#     i += 1
#
# available_exits = ["east", "north east", "south"]
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over!")
#         break
# else:
#     print("Aren't you glad you got out of there?!?!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {0}".format(highest))
guess = int(input())

while guess != answer:
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    guess = int(input())
else:
    print("You guessed it!")


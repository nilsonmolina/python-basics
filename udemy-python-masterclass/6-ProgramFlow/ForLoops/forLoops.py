# for i in range(1, 20):
#     print("i is now {}".format(i))
#
# number = "9,255,192,168,131,589,808"
# for i in range(0, len(number)):
#     print(number[i])


# number = "9,255,192,168,131,589,808"
# cleanedNumber = ""
#
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is: {}".format(newNumber))


# # ------- PART 2 -------
# number = "9,255,192,168,131,589,808"
# cleanedNumber = ""
#
# for char in number:
#     if char in "0123456789":
#         cleanedNumber += char
#
# print("New number is: {}".format(int(cleanedNumber)))


# for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
#     print("This parrot is " + state)
#     # print("This parrot is {}".format(state))


# for i in range(0, 100, 5):
#     print("i is {}".format(i))


for i in range(1, 13):
    for j in range(1, 13):
        print("{0:2} times {1:2} is {2:3}".format(i, j, i*j))
    print("==================")

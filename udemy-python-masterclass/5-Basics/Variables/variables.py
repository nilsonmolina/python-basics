# # integer - whole number - computations faster than floating point number
# a = 12
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)  # returns as a float
# print(a // b)  # returns as an integer
# print(a % b)
#
# for i in range(1, a / b):  # requires a // b
#     print('loop: ' + str(i))
#
# print(a + b / 3 - 4 * 12)

parrot = 'Norwegian Blue'
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])  # starts at the back end of the string
print(parrot[0:6])  # [s:e] - starts at index s & includes up to, but not including character at index position a
print(parrot[:6])
print(parrot[0:])
print(parrot[-4:2])  # cannot go backwards from the starting position with this context
print(parrot[-4:-2])
print(parrot[0:6:2])  # [s:e:i] - start at s : end at, but don't include e : do in increments of i
print(parrot[0:6:3])  # [s:e:i] - start at s : end at, but don't include e : do in increments of i

number = '9,223,131,213,237,975'
print(number[1::4])  # prints out only the commas due to the increments
print(number[1:-1:4])  # I believe this is equivalent

numbers = '1, 2, 3, 4, 5, 6, 7, 8, 9'
print(numbers[0::3])

string1 = "he's "
string2 = 'probably '
print(string1 + string2)
print("he's " "probably ")  # not really useful, but it can be done

print("Hello " * 5)

today = "friday"
print("day" in today)
print("fri" in today)
print("fri" in today)
print("fri " in today)

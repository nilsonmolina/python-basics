age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))

# The following is deprecated and was used in python 2
print("My age is %d years" % age)
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i**2, i**3))

print("PI is approximately %12f" % (22 / 7))
print("PI is approximately %12.50f" % (22 / 7))

# Performing the same as deprecated, but with the new format
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:<4}".format(i, i**2, i**3))

print("PI is approximately {0:12.50}".format(22 / 7))

# Note that if you do not put a value in the brackets, python will assume order
print("This {} a {}!".format("is", "test", "n/a"))

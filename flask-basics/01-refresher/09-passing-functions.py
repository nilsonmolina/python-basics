""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

# Passing Functions
print(f"""--------------------------
Passing Functions
--------------------------""")
my_list = [13, 56, 77, 484]

def not_thirteen(x):
    """ Why would someone want a method like this? """
    return x != 13

print(list(filter(lambda x: x != 13, my_list)))
print(list(filter(not_thirteen, my_list)))
print([x for x in my_list if x != 13])

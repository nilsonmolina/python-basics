""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

print(f"""
what are args?
---------------""")
def my_long_sum(arg1, arg2, arg3, arg4, arg5):
    """ Sums 5 separate arguments together """
    return arg1 + arg2 + arg3 + arg4 + arg5

def my_list_sum(list_arg):
    """" Sums a list of 5 arguments together """
    return sum(list_arg)

print(my_long_sum(3, 5, 7, 13, 4))
print(my_list_sum([3, 5, 7, 13, 4]))

print(f"""
what are kwargs?
---------------""")

def what_are_kwargs(*args, **kwargs):
    """" Prints args and kwargs """
    print(args)
    print(kwargs)

def out_of_order(name, location):
    """" kwargs can be out of order """
    print(name)
    print(location)

what_are_kwargs(13, 27, 8, name='Jose', location='UK')
print("")
out_of_order(location='UK', name='Jose')

""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103,C0111
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.
# - [C0111] is a warning when missing function docstrings.

import functools

# BASIC DECORATOR
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("Basic decorator start!")
        func()
        print("Basic decorator end!\n")
    return function_that_runs_func

# ADVANCED DECORATOR
def decorator_with_args(number):
    def my_new_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("Starting Adv Decorator")
            if number != 13:
                print("Number not good enough! Try another.")
            else:
                func(*args, **kwargs)
            print("Ending Adv Decorator\n")
        return function_that_runs_func
    return my_new_decorator

# Functions to use w/ decorators
@my_decorator
def my_function():
    print("I'm the function!")

@decorator_with_args(1)
def my_function_too():
    print("I'm also a function!")

@decorator_with_args(13)
def my_function_thrice(x, y):
    print("I'm also a function!", x + y, x * y)

# Running it all
my_function()
my_function_too()
my_function_thrice(6, 7)

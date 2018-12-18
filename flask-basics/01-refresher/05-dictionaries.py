""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

# List Comprehension
print("--------------------------")
print("Dictionaries")
print("--------------------------")
my_dict = {'name': 'Nilson', 'age': 90, 'grades': [89, 93, 96, 72]}
lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 42, 33, 66, 27)
}
universities = [
    {'name': 'Oxford', 'location': 'UK'},
    {'name': 'MIT', 'location': 'US'}
]

print(f"""
- Dictionaries are a set of Key/Value pairs.
my_dict = {{'name': 'Nilson', 'age': 90, 'grades': [89, 93, 96, 72]}}

- We can have tuples inside Dictionaries
lottery_player = {{
    'name': 'Rolf',
    'numbers': (13, 42, 33, 66, 27)
}}

- We can have a list of Dictionaries
universities = [
    {{'name': 'Oxford', 'location': 'UK'}},
    {{'name': 'MIT', 'location': 'US'}}
]

- Unlike a set, we can access elements within
sum(lottery_player['numbers']): {sum(lottery_player['numbers'])}
""")

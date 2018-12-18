""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

# List Comprehension
print("--------------------------")
print("List Comprehension")
print("--------------------------")
my_list = [0, 1, 2, 3, 4]
equal_list_1 = [x for x in range(5)]
equal_list_2 = list(range(0, 5))
multiply_list = [x * 3 for x in range(5)]
evens_list = [n for n in range(10) if n % 2 == 0]
odds_list = [n for n in range(1, 10, 2)]

known_people = ["Linh", "mArk", " Edouard", "PARAS"]
normalized_known_people = [p.strip().lower() for p in known_people]


print(f"""
my_list:       {my_list}
equal_list_1:  {equal_list_1}
equal_list_2:  {equal_list_2}
multiply_list: {multiply_list}
evens_list:    {evens_list}
odds_list:     {odds_list}

known_people:  {known_people}
normalized:    {normalized_known_people}
""")

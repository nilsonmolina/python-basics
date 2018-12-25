# Python Basics

This repo holds projects I worked on while learning the basics of python.

The README is very much a rough draft. Just did a quick brain dump to get a template of sorts.

# Python Basics
### **[Lists](https://nilsonmolina.github.io/python-basics/flask-basics/01-refresher/01-lists-tuples-sets.py)**  
- Ordered
- Mutable (can be changed)

```python
list_of_grades = [90, 77, 80, 90]

# --- Basic Operations ---
print(list_of_grades)
# [90, 77, 80, 90]
len(list_of_grades)
# 4
sum(list_of_grades)
# 337
list_of_grades[0]
# 90
list_of_grades[0] = 60
# [60, 77, 80, 90]
list_of_grades.append(100)
# [60, 77, 80, 90, 100]
```

### **[Tuples](https://nilsonmolina.github.io/python-basics/flask-basics/01-refresher/01-lists-tuples-sets.py)**
- Ordered
- Immutable (cannot be changed)

```python
tuple_of_grades = (90, 77, 80, 90)

# --- Basic Operations ---
print(tuple_of_grades)
# (90, 77, 80, 90)
len(tuple_of_grades)
# 4
sum(tuple_of_grades)
# 337
tuple_of_grades[0]
# 90
tuple_of_grades[0] = 60
# Traceback: 'tuple' does not support item assignment
tuple_of_grades.append(100)
# Traceback: 'tuple' object has no attribute 'append'

### A workaround for appending a tuple is to redefine its value as shown below
tuple_of_grades = tuple_of_grades + (100,)
# (90, 77, 80, 90, 100)

```

### **[Sets](https://nilsonmolina.github.io/python-basics/flask-basics/01-refresher/01-lists-tuples-sets.py)**

- Unordered
- Immutable
- Unique
```python
set_of_grades = {90, 77, 80, 90}

# --- Basic Operations ---
print(set_of_grades)
# {80, 90, 77}
len(set_of_grades)
# 3
sum(set_of_grades)
# 247
set_of_grades[0]
# Traceback: 'set' object does not support indexing
set_of_grades[0] = 60
# Traceback: 'set' object does not support item assignment
set_of_grades.append(100)
# Traceback: 'set' object has no attribute 'append'

### A workaround for appending a set is to use the 'add' method as shown below
set_of_grades.add(100)
# {80, 90, 100, 77}
```

### **[Dictionaries](https://nilsonmolina.github.io/python-basics/flask-basics/01-refresher/05-dictionaries.py)**
Dictionaries are a key/value set. The value in a dictionary can be pretty much any datatype, even lists, tuples, etc... 
```python
### We can have lists inside Dictionaries
my_dict = { 'name': 'Nilson', 'age': 90, 'grades': [89, 93, 96, 72] }

### we can have tuples inside Dictionaries
lottery_player = {
  'name': 'Rolf',
  'numbers': (13, 42, 33, 66, 27)
}

### We can have a list of Dictionaries
universities = [
  { 'name': 'Oxford', 'location': 'UK' },
  { 'name': 'MIT', 'location': 'US' }
]

### Unlike a set, we can access elements within
sum(lottery_player['numbers'])
# 181

```

### **[Classes](https://nilsonmolina.github.io/python-basics/flask-basics/01-refresher/06-classes.py)**
Classes are not dictionaries. Classes always start with a capital letter.
```python
class Lottery_Player:
  def __init__(self, name):
    self.name = name
```
### **[Args and Kwargs](https://nilsonmolina.github.io/python-basics/flask-basics/01-refresher/07-args-kwargs.py)**
**Passing Multiple Arguments**  
There comes a point where you need to pass many parameters, but dealing with them can seem both unwieldy and sloppy.
```python
def my_long_sum(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

print(my_long_sum(3, 5, 7, 13, 4))
# 32
```
However, what if you do NOT know how many arguments will be passed or you want to allow a variable number of arguments to be passed? By using *args, we can do just that.
```python
def simplified_sum(*args):
  return sum(args)

print(simplified_sum(3, 5, 7, 13, 4))
# 32
```

**What are kwargs?**  
kwargs stands for "Key Word Arguments"
```python
def what_are_kwargs(*args, **kwargs):
  print(args)
  print(kwargs)

def out_of_order(name, location):
  """" kwargs can be out of order """
  print(name)
  print(location)

what_are_kwargs(13, 27, 8, name='Jose', location='UK')
# (13, 27, 8)
# {'name': 'Jose', 'location': 'UK'}

out_of_order(location='UK', name='Jose')
# Jose
# UK
```
### Coding Exercise
```python
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count
```

```python
class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item['price'] for item in self.items])

        # w/o list comprehension
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return total

```

# Flask Basics

### Virtual Environments
Similar to npm, allows us to keep our dependencies on a per project level. There are two ways to create a virtual environment:
```bash
# Navigate to your projects root folder and then run this command:
$ python3 -m venv venv

# Or install virtualenv and create it directly:
$ pip3 install virtualenv
$ virtualenv venv
```
*_On my machine, the first method would create the venv with an old version of pip (9.0), but the second method installed it with the latest version of pip (18.1)._

**To activate or deactivate the virtual environment, run the following commands:**
```bash
# Activate
$ . venv/bin/activate

# Deactivate
$ deactivate
```
*_You will know if you are in the virtual environment if your console shows `(venv)` at the start of the command line._
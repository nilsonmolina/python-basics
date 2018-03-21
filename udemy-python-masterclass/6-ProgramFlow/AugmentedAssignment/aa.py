# Augmented Assignment in Python actually has a performance improvement over writing out the full expression.
# For example, given 'x = x + 1', Python actually creates a new x variable to store the data, and then destroys
# the previous x data from memory. By using 'x += 1' Python simply evaluates the expression.

# += -= *= /= %= **= <<= >>= &= ^= |=

x = 23

# x = x + 1
x += 1
print(x)

# x = x - 4
x -= 4
print(x)

# x = x * 5
x *= 5
print(x)

# x = x / 4
x /= 4
print(x)

# x = x ** 2
x **= 2
print(x)

# x = x % 60
x %= 60
print(x)


greeting = "Good "

greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)

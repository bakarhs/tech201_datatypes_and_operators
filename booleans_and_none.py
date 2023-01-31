# # Booleans

# # True ot False
# Remember to capitalise!

# a = True
# b = False

# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True - true is considered greater than false
# print(b <= False) # True

# print(True and False) # False - evaluates and as both sides being ture ( only way to return true is with 'True and True'
# print(False and True) # False
# print(False or True) # True - because true is available it will go for true

# Booleans are useful for quickly checking the state of something.
# The other area Booleans are relly useful are validating data types

# Booleans with Data types

hi = "Hello world!"

print(hi.isalpha()) # False - contains a space and a ! which is not alphanumeric
print(hi.islower()) # False - starts with a capital H
print(hi.isupper()) # False - text is mostly lowercase
print(hi.endswith("!")) #True
print(hi.startswith("Hello")) #True

x = 1
y = 10
z = -15
print(bool(x)) # False - 0 is always False
print(bool(y)) # True
print(bool(z)) # True

# None

# None == Null in a lot of other languages


print (bool(None)) # False

x = None

print(x == False) # False
print(x == True) # False

# Checking if a variable is None

print(x == None) # direct comparison - more complex situation.
print(x is None) # Best practise for checking if something 'is None'

print(type(x)) # <class 'NoneType'>




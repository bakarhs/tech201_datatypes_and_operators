# tech201_datatypes_and_operators
tech201_datatypes_and_operators

# Data types
Numeric - Ints, Floats, longs  (no longer needed), complex
String - Text of any type
Boolean - True or False

## Operators

### Artithmatic operators
 : + , - ,*, /

### Comparison operators
```
 > = greater than
 < = less than
 == = is equal to
 != = is not equal to
 >= = greater than or equal to
 <= = less than or equal to
```
## Implementing numeric types

### Integers
Example:
```
a = 24
b = 16

print(a + b) # 40
print(a > b) # True
print(a < b) # False
```

## Floats
```
FloatNum = 1.356
IntNum = 4

print( FloatNum + IntNum) # 5.356
```

There's no limit to the size of a decimal, but Python will round thing up
```
one_third = 1 / 3
print(one_third) # 0.3333333333

print (one_third * 3) # 1.0
```

# Strings
Example of string:
```
Single_quotes = 'Look! single quotes'
Double_quotes = "Look! double quotes"

print(Single_quotes)
print(Double_quotes)
```
## String failure
Example of string failure
```
string_failure = 'I said 'wow!''
```
## Escaping string failure
Examples:
```
escape_example = 'I said  \'Wow\''
print(escape_example)
quote_in_quote = 'I said "wow!"'
print(quote_in_quote)
reverse_quote = "I said 'wow!'"
print(reverse_quote)
```

## String slicing
Everything in code starts with 0 not 1
H e l l o   W o r l d  !
0 1 2 3 4 5 6 7 8 9 10 11

Examples of string slicing:
```
Hw = "Hello World!"
print(Hw[7: ]) # orld!
print(Hw[-5:]) # orld!
print(Hw[ :5]) # Hello
print(Hw[0:5]) # Hello
```

## String methods

### How to use strip() to remove white spaces
```
white_space = "lot's of space at the end                                             "
print(len(white_space)) # 70
print(len(white_space.strip())) # 25
```
## A few more examples of what we can do

This is the example text we will be using


`example_text = "Here's some text with lot's of text"`

### How to Count a substring within a string
`print(example_text.count("text")) #2`

# Make everything lowercase

`print (example_text.lower())`

# Make everything uppercase

`print(example_text. upper())`

# Capitalise text

`print(example_text.capitalize())`

# Replace characters / text
print(example_text.replace("with" , ","))

# Concatenation

a = "here "
b = "more "
c = "much more"

print(a + b + c)

# Casting

x = 2
y = 5.4
z = " there's a number 25.4 unless we put a space!"

#print(x + y +z)
print(str(x) + ", " + str(y) + z)

# string to numeric

int_string = "6"

print(int (int_string))
print(type(int(int_string)))

# This also works with float
float_string = "6"

print(float(float_string))
print(type(float(float_string)))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm}cm tall")

# F-string allows us to use methods/evaluations too

name = "Snoopy"
years = 52

print(f"{name.upper()} Is {years * 7} years old in dog years!!!!!")

# F=string to specify precision in rounding and decimals

pi = 3.1415926359

print(f"Pi to 3 decimal places: {pi:.3f}") #Pi to 3 decimal places
print(f"Pi to 3 decimal places: {pi:.5f}") #Pi to 5 decimal places

score = 16
max_score = 26

print(f"You scored {score/max_score}") # 0.6153846153846154
print(f"You scored {score/max_score:%}") # 61.538462%
print(f"You scored {score/max_score:.2%}") # 61.54%
print(f"You scored {score/max_score:.0%}")



# Complete the exercises below by writing an expression in Python to
# answer the question:
# 1. Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"
print(first)

# 2. Write a comment that says "This is a comment."
# "This is a comment."

# 3. Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

# 4. Write an if statement that checks if 1 is less than 2 and if 4 is
# greater than 2. If it is, show the message "Math is fun."`
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# 5. Assign a variable called nope to an absence of value.
nope = None
print(nope)

# 6. Use the language's "and" boolean operator to combine the language's
# "true" value with its "false" value.
bools = True and False
print(bools)

# 7. Calculate the length of the string "What's my length?"
what_length = "What's my length?"
print("{}: {}").format(what_length, len(what_length))

# 8. Convert the string "i am shouting" to uppercase.
print("i am shouting".upper())

# 9. Convert the string "1000" to the number 1000.
print(int("1000"))

# 10. Combine the number 4 with the string "real" to produce "4real".
print(str(4) + "real")

# 11. Record the output of the expression 3 * "cool".
print(3 * "cool")
# coolcoolcool

# 12. Record the output of the expression 1 / 0.
# print(1 / 0)
# Traceback (most recent call last):
#   File "booleanLogic.py", line 44, in <module>
#     print(1 / 0)
# ZeroDivisionError: integer division or modulo by zero

# 13. Determine the type of [].
print(type([]))  # list

# 14. Ask the user for their name, and store it in a variable called name.
name = input("What is your name? ")

# 15. Ask the user for a number. If the number is negative, show a message
# that says "That number is less than 0!" If the number is positive, show
# a message that says "That number is greater than 0!" Otherwise, show a
# message that says "You picked 0!.
number = float(input("Input a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

# 16. Find the index of "l" in "apple".
print("The index of 'l' in 'apple' is: {}").format("apple".index("l"))

# 17. Check whether "y" is in "xylophone".
if "xylophone".find("y") != -1:
    include = "yes"
else:
    include = "no"
print("Is 'y' in 'xylophone?: {}").format(include)

# 18. Check whether a string called my_string is all in lowercase.
my_string = "this is a String"
if my_string == my_string.lower():
    lower = "yes"
else:
    lower = "no"
print("Is 'this is a String' all lowercase?: {}").format(lower)

# Part I
# Write the following Python code to do the following (complete ALL of
# these using list comprehension).

# 1. Given a list [1,2,3,4], print out all the values in the list.
print([val for val in [1, 2, 3, 4]])

# 2. Given a list [1,2,3,4], print out all the values in the list
# multiplied by 20.
print([num * 20 for num in [1, 2, 3, 4]])

# 3. Given a list ["Elie", "Tim", "Matt"], return a new list with only the first
# letter (["E", "T", "M"]).
print([letter[0] for letter in ["Elie", "Tim", "Matt"]])

# 4. Given a list [1,2,3,4,5,6] return a new list of all the even values
# ([2,4,6]).
print([num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0])

# 5. Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the
# intersection of the two ([3,4]).
print([num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]])

# 6. Given a list of words ["Elie", "Tim", "Matt"] return a new list with each
# word reversed and in lower case (['eile', 'mit', 'ttam']).
print([name[::-1].lower() for name in ["Elie", "Tim", "Matt"]])

# 7. Given two strings "first" and "third", return a new string with all the
# letters present in both words (["i", "r", "t"]).
print([letter for letter in "first" if letter in "third"])

# 8. For all the numbers between 1 and 100, return a list with all the numbers
# that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
print([num for num in range(1, 100) if num % 12 == 0])

# 9. Given the string "amazing", return a list with all the vowels removed
# (['m', 'z', 'n', 'g']).
print([vowel for vowel in "amazing" if vowel not in ['a', 'e', 'i', 'o', 'u']])

# 10. Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
# print([[val for val in range(0, 3)]] * 3)
print([[val for val in range(0, 3)] for num in range(0, 3)])

# 11. Generate a list with the value:
#     [
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     ]
# print([[val for val in range(0, 10)]] * 10)
print([[val for val in range(0, 10)] for num in range(0, 10)])

# Part II
# Complete the following Codewars problems:

# Reversed Strings

# Looking for a benefactor

# Sum of a sequence

# Max diff

# Count the similey faces!

# Sentence Count

# Tortoise Racing

# Calculate String Rotation

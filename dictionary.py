# Write the following Python code to do the following (Complete ALL of the
# following using dictionary comprehension)

# 1. Given a list[("name", "Elie"), ("job", "Instructor")], create a dictionary
# that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not
# matter).
a_list = [("name", "Elie"), ("job", "Instructor")]
print({key: value for key, value in a_list})

# 2. Given two lists["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode
# Island"] return a dictionary that looks like this {'CA': 'California',
# 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. You can research the zip method to
# help you.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
print(dict(zip(list1, list2)))

# 3. Create a dictionary with the key as a vowel in the alphabet and the value
# as 0. Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0,
# 'u': 0}. (Do not use the fromkeys method).
print({key: 0 for key in ['a', 'e', 'i', 'o', 'u']})

# 4. Create a dictionary starting with the key of the position of the letter
# and the value as the letter in the alphabet. You should return something
# like this (Hint - use chr(65) to get the first letter):
# {1: 'A',
#  2: 'B',
#  3: 'C',
#  4: 'D',
#  5: 'E',
#  6: 'F',
#  7: 'G',
#  8: 'H',
#  9: 'I',
#  10: 'J',
#  11: 'K',
#  12: 'L',
#  13: 'M',
#  14: 'N',
#  15: 'O',
#  16: 'P',
#  17: 'Q',
#  18: 'R',
#  19: 'S',
#  20: 'T',
#  21: 'U',
#  22: 'V',
#  23: 'W',
#  24: 'X',
#  25: 'Y',
#  26: 'Z'}

print({i-64: chr(i) for i in range(65, 65+26)})

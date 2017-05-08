# Part I
# Write the following functions

# difference
# this function takes in two parameters and returns the difference between
# the two
def difference(a, b):
    return a - b

# print(difference(2, 2))  # 0
# print(difference(0, 2))  # -2

# product
# this function takes in two parameters and returns the product of the two
def product(a, b):
    return a * b

# print(product(2, 2))  # 4
# print(product(0, 2))  # 0

# print_day
# this function takes in one parameter (a number from 1-7) and returns the day
# of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.). If the number is
# less than 1 or greater than 7, the function should return None
def print_day(a: int):
    day_of_week = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    if a in day_of_week:
        return day_of_week[a]

# print(print_day(4))  # "Wednesday"
# print(print_day(41))  # None

# last_element
# this function takes in one parameter (a list) and returns the last value in
# the list. It should return None if the list is empty.
def last_element(l: list):
    if l == []:
        return None
    if l[-1]:
        return l[-1]

# print(last_element([1, 2, 3, 4]))  # 4
# print(last_element([]))  # None

# number_compare
# this function takes in two parameters (both numbers). If the first is greater
# than the second, this function returns "First is greater." If the second
# number is greater than the first, the function returns "Second is greater."
# Otherwise the function returns "Numbers are equal."
def number_compare(a, b) -> str:
    if (a == b):
        return "Numbers are equal"
    elif (a > b):
        return "First is greater"
    return "Second is greater"

# print(number_compare(1, 1))  # "Numbers are equal"
# print(number_compare(1, 2))  # "First is greater"
# print(number_compare(2, 1))  # "Second is greater"

# single_letter_count
# this function takes in two parameters (two strings). The first parameter
# should be a word and the second should be a letter. The function returns the
# number of times that letter appears in the word. The function should be case
# insensitive (does not matter if the input is lowercase or uppercase). If the
# letter is not found in the word, the function should return 0.
def single_letter_count(string: str, char: str) -> int:
    return string.lower().count(char.lower())

# print(single_letter_count('amazing', 'A'))  # 2

# multiple_letter_count
# this function takes in one parameter (a string) and returns a dictionary with
# the keys being the letters and the values being the count of the letter.
def multiple_letter_count(string: str) -> dict:
    return {char: string.count(char) for char in string}

# print(multiple_letter_count("hello"))  # {h:1, e: 1, l: 2, o:1}
# print(multiple_letter_count("person"))  # {p:1, e: 1, r: 1, s:1, o:1, n:1}

# list_manipulation
# this function should take in three parameters (a list, command, location and
# value).
# -If the command is "remove" and the location is "end", the function should
# remove the last value in the list and return the value removed
# -If the command is "remove" and the location is "beginning", the function
# should remove the first value in the list and return the value removed
# -If the command is "add" and the location is "beginning", the function should
# add the value (fourth parameter) to the beginning of the list and return the
# list
# -If the command is "add" and the location is "end", the function should add
# the value (fourth parameter) to the end of the list and return the list
def list_manipulation(l: list, command: str, location: str, *val):
    if command == "remove" and location == "end":
        return l.pop()
    if command == "remove" and location == "beginning":
        return l.pop(0)
    if command == "add" and location == "beginning":
        l.insert(0, *val)
        return l
    if command == "add" and location == "end":
        l.append(*val)
        return l

# print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
# print(list_manipulation([1, 2, 3], "remove", "beginning"))  # 1
# print(list_manipulation([1, 2, 3], "add", "beginning", 20))  # [20,1,2,3]
# print(list_manipulation([1, 2, 3], "add", "end", 30))  # [1,2,3,30]

# is_palindrome
# A Palindrome is a word, phrase, number, or other sequence of characters which
# reads the same backward or forward. This function should take in one
# parameter and returns True or False depending on whether it is a palindrome.
# As a bonus, allow your function to ignore whitespace and capitalization so
# that is_palindrome('a man a plan a canal Panama') returns True.
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

# print(is_palindrome('testing'))  # False
# print(is_palindrome('tacocat'))  # True
# print(is_palindrome('hannah'))  # True
# print(is_palindrome('robert'))  # False

# frequency
# This function accepts a list and a search_term (this will always be a
# primitive value) and returns the number of times the search_term appears in
# the list.
def frequency(l: list, search_term) -> int:
    return l.count(search_term)

# print(frequency([1, 2, 3, 4, 4, 4], 4))  # 3
# print(frequency([True, False, True, True], False))  # 1

# flip_case
# This function accepts a string and a letter and reverses the case of all
# occurances of the letter in the string.
def flip_case(s: str, letter: str) -> str:
    new_string = ""
    new_letter = letter.lower()
    for char in s:
        if letter in char:
            new_string += new_letter.upper()
        elif letter.upper() in char:
            new_string += new_letter
        else:
            new_string += char
    return new_string

# print(flip_case("Hardy har har", "h"))  # "hardy Har Har"

# multiply_even_numbers
# This function accepts a list of numbers and returns the product of all even
# numbers in the list.
def multiply_even_numbers(l: list):
    even_product = 1
    for num in l:
        if num % 2 == 0:
            even_product *= num
    return even_product

# print(multiply_even_numbers([2, 3, 4, 5, 6]))  # 48

# mode
# This function accepts a list of numbers and returns the most frequent number
# in the list of numbers. You can assume that the mode will be unique.

# this definitely can be refactored
def mode(l: list):
    d = {num: l.count(num) for num in l}
    count = 0
    for key, value in d.items():
        if value > count:
            count = value
            frequent = key
    return frequent

# print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))  # 4

# capitalize
# This function accepts a string and returns the same string with the first
# letter capitalized.
def capitalize(s: str) -> str:
    # return s.capitalize() # haha... no
    return s[:1].upper() + s[1:]

# print(capitalize("tim"))  # "Tim"
# print(capitalize("matt"))  # "Matt"

# compact
# This function accepts a list and returns a list of values that are truthy
# values.
def compact(l: list) -> list:
    return [val for val in l if val]

# print(compact([0, 1, 2, "", [], False, {}, None, "All done"])) # [1,2,
# "All done"]

# partition
# This function accepts a list and a callback function (which you can assume
# returns True or False). The function should iterate over each element in the
# list and invoke the callback function at each iteration. If the result of the
# callback function is True, the element should go into one list if it's False,
# the element should go into another list. When it's finished, partition should
# return both lists inside of one larger list.
def is_even(num):
    return num % 2 == 0

def partition(l: list, fn: bool) -> list: 
    # not pythonic enough
    # true_list = []
    # false_list = []
    # for element in l:
    #     if (fn(element)):
    #         true_list.append(element)
    #     else:
    #         false_list.append(element)
    # return [true_list, false_list]
    return [[e for e in l if fn(e)], [e for e in l if not fn(e)]]

# print(partition([1, 2, 3, 4], is_even))  # [[2,4],[1,3]]

# intersection
# This function should accept a two dimensional list and return a list with the
# values that are the same in each list.
def intersection(l1: list, l2: list) -> list:
    return [val for val in l1 if val in l2]

# print(intersection([1, 2, 3], [2, 3, 4]))  # [2,3]

# once
# This function accepts a function and returns a new function that can only be
# invoked once. If the function is invoked more than once, it should return
# None. Hint you will need to define a new function inside of your once
# function and return that function. You can add properties to your inner
# function to see if it has run already.
def add(a, b):
    return a + b

def once(fn):
    def inner(*args):
        inner.count += 1
        if (inner.count <= 1):
            return fn(*args)
    inner.count = 0
    return inner

# one_addition = once(add)
# print(one_addition(2, 2))  # 4
# print(one_addition(2, 2))  # undefined
# print(one_addition(12, 200))  # undefined

# Super bonus
# Research what decorators are and refactor your once code to use a decorator
# so that you can run

from functools import wraps
def run_once(fn):
    wraps(fn)
    def inner(*args):
        inner.count += 1
        if (inner.count <= 1):
            return fn(*args)
    inner.count = 0
    return inner

@run_once
def add_again(a, b):
    return a + b

# print(add_again(2, 2))  # 4
# print(add_again(12, 20))  # None
# print(add_again(2, 20))  # None

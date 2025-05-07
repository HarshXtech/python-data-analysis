# Strings are collection of characters
# A string is a content that is written inside either single quote, double quote or triple quote. 
# strings are immutable / unchangeable
# Strings can be accessed by indexing (indexing starts from 0)
# length starts from 1

info = "Hello, world"

# print(type(info))

# info[0] = 'W'
# print(info)


# methods of strings!

# upper : it converts entire string into uppercase letters
# print(info.upper())

# lower : it converts entire string into lowercase letters
# print(info.lower())

# count : to count certian number of characters
# print(info.count('o'))

# lenth of the string :
# print(len(info))

# replace : used to replace any word/character
# print(info.replace('world', 'python'))

# to check if the variable starts with any perticular value/character
# print(info.startswith('H'))

# to check if the variable ends with any perticular value/character
# print(info.endswith('d'))

# what are real world application of the string and its methods?

# taking inputs from user : string formate. 

# username = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(username)
# print(age)

# formate. 

# how to write/print variable's value inside a string
# this format is not readable
# info = "My name is " + username + " and my age is " + age + " ."

# info = "My name is {}. and my age is {}".format(username, age)

# info = f'my name is {username} and my age is {age}'

# type casting / type conversion

# print(type(username))
# print(type(age))


# to learn real world use-cases

# what are some real world applications of type casting and string methods!
# uppercase, lowercase, count, len

# uppercase : coupen codes / discount codes 
# lowercase : username, email, url : 
# len : your password needs to be of at least 8 char.
# count : 1 special, 1 lower, 1 upper, 1 int

# convert or change the data-type of a variable?


# user inputs are in string by default

# age = int(input("Enter your age: "))

# 10 > harsh
# print(age > 18)
# print(type(age))

# task : 

# string to boolean
# boolean to string
# int to boolean
# boolean to int
# string to int
# int to string

# 0 into boolean -> False
# mark = "0"

# print(bool(mark))

isConfirmed = False


print(int(isConfirmed))
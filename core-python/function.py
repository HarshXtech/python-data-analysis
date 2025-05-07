# function : 

# There are two types of function!
# functions are block of code that help us to perform a specific task!


# 1) built-in / in-built functions : print, len, add, pop, intersection, union, append, type
# 2) user-defined function! : we can create our own functions as per our requirments.

# create a function that adds two digits

# define
# def function_name(arguments):
    # code goes here... 
    # pass


# def sum(a, b=10):
#     print(a + b)

# sum(10)

# sum(10, 20)
# sum(30, 40)
# sum(3100, 200)


# def is a keyword to declare a function
# sum is a name of the functions
# a, and b are arguments
# print(a+b) : operation, task to be performed by function


# create a function to greet user

# def greet():
#     username = input("Enter your name: ")
#     print(f'Hello, {username}')

# greet()


# what are global and local variables?


# global variable : a variable that is declared outside of the function, is global variable :
# can be accessed from anywhere in the script


# a = 10
# a = 30

# local variable : a variable that is declared inside a function, is a local variable
# local variable can be accessed from inside the function only!


# def myFunc():
#     global a
#     a = 30
    # print(a)

# myFunc() # accessing the value of local variable

# print(a) # 10 , 30 ? 
# myFunc()
# print(a) # accessing the value of global variable


# how we convert a local variable into global variable?

# indentation (space) in function!
        

# def greet():
#     print('hello world')

# return statement


# def greet():
    # print('Hello world')
    # return "Hello world"


# print(greet() + " Hello")


# def sum(a,b):
    # print(a + b)
    # return a + b


# calling function / invoking the function
# sum(10, 20)

# print(sum(10, 20))
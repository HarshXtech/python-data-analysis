# check if the given number is odd or even!

# 1,3,5,7,9  : odd numbers
# 2,4,6,8,10 : even numbers

user = int(input('Enter a number: '))

# camelCase : 
# class name : PacalCase


def checkOddEven(n):
    if n < 0:
        print("Negative number")
    elif n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

checkOddEven(user)
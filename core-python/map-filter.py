# map and filter function : 

def myFunc(n):
    return n**2

a = [1,2,3,4,5,6,7]

# map function helps us to execute a specific function to the all elements present in the list

# answer = list(map(myFunc, a))

# print(answer)

# output = list(map(lambda x : x**2, a))

# print(output)


# filter method

# def filterEvenNumber(n):
#     return n % 2 == 0

# answer = list(filter(filterEvenNumber, a))

# print(answer)

output = list(filter(lambda x : x % 2 != 0, a))

print(output)
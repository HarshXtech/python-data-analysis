# dictionary : collection of keys and values pair
# they are mutable/changeable
# they can be accessed by its keys
# they are ordered ( in the second version of python, they used to be unordered )
# denoted by {}

# employee = {
#     'name' : 'Harsh',
#     'prof' : 'Python developer',
#     'salary' : 10
# }

# print(type(employee))

# keys == indexing
# print(employee['salary'])

# print(employee)

# methods of dictionary


# by passing a key of the dict, it will give us the value of that key
# print(employee.get('name'))

# print(employee.items())
# print(employee.keys())
# print(employee.values())


# clear : clear our dictionary
# employee.clear()
# print(employee)


# employee['name'] = 'Shubh'

# employee['city'] = 'NYC'
# print(employee)

# employee.pop('name')
# print(employee)

# nested dictionary : dict inside dict

employee = {
    'name' : 'Harsh',
    'google' : {
        'id' : 10,
        'role' : 'analyst',
        'salary' : 5
    },
    'age' : 100
}

print(employee['google']['role'])
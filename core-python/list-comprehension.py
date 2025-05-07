a = [1,2,3,4,5,6,7]

# sqaure = []

# def square_values(lst):
#     for i in lst:
#         sqaure.append(i**2)
#     return sqaure


# print(square_values(a))

# even = []
# def even_numbers(lst):
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#     return even


# print(even_numbers(a))

country = ['india', 'usa', 'uk', 'japan']

# upper_countries = []
# def convert_to_upper(lst):
#     for i in lst:
#         upper_countries.append(i.upper())

#     return upper_countries

# print(convert_to_upper(country))

x = [1,2,3,4,5,6,7]

# sqaure = [i**2 for i in x]
# print(sqaure)

# even = [i for i in x if i % 2 == 0]
# print(even)


upper_countries = [i.upper() for i in country]
print(upper_countries)
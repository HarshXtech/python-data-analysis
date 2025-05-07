

# r : read
# file = open('info.txt', 'r')

# print(file.read())

# with open('info.txt', 'r') as file:
#     print(file.read())


# with open('info.txt', 'w') as file:
#     file.write("This is new content from python language!")

# to append data / to update the file
# with open('info.txt', 'a') as file:
#     file.write("\nThis is a content to be appended!")

# with open('details.txt', 'w') as file:
#     file.write("This is details.txt file")

# delete : 

import os # operating system
import shutil

# user = input("Do you want to delete this file? y/n")

# if user == 'y':
#     os.remove('details.txt')
#     print("Your file has been deleted successfully!")
# else:
#     print("Your file not removed!")


# CRUD : create, read, update, delete!

# folders!
# directory : folder
# os.rmdir('myfolder') 

# rmdir method deletes only empty dir
# os.rmdir('myfolder')

# how to remove non-empty folder : 

shutil.rmtree('myfolder')

# text, csv, excel, npy, html
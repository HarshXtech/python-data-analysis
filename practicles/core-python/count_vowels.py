# AEIOU

def count_vowels(string):

    vowels = 'aeiou'
    total_vowels = 0

    for i in string.lower():
        if i in vowels.lower():
            total_vowels += 1

    return total_vowels


print(count_vowels('Harsh and Python language'))

# a = 'python'

# for char in a:
#     print(char)

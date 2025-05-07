# 1534 : 

# 3 

# 1 ** 3 : 1 
# 5 ** 3 : 125
# 3 ** 3 : 27


# 370 : 

# 3

# 3 ** 3
# 7 ** 3 : 
# 0 ** 3 : 0

def checkArmStrongNumber(n):
    length = len(str(n))
    
    total = sum([int(i) ** length for i in str(n)])

    return total == n


print(checkArmStrongNumber(370))

# num = '154'

# for i in num:
#     print(i)

# 153 : 


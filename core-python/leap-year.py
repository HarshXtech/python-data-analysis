# check if the given year is leap year or not!

# 2000, 2004, 2008, 2012, 2016, 2020, 2024 : 366

year = int(input("Enter a year: "))


# all centuries : 100, 200, 1000, 2000, 2100 : 
# not all centuries are leap year, but all centuries can be devided by 4

# 100, 200, 300, 400, 500, 600, 700, 800

# 400
# 800
# 1200
# 1600
# 1700
# 1800
# 1900
# 2000

def checkLeapYear(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(checkLeapYear(year))
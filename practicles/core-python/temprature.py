def temprature_converter(value, unit):

    if unit.lower() == 'f':
        celcius = (value - 32) * 5/9
        return round(celcius)
    elif unit.lower() == 'c':
        fahrenheit = (value * 9/5) + 32
        return round(fahrenheit)
    else:
        raise ValueError("Invalid values!")


print(temprature_converter(100, 'a'))

def square(number):
    acumulador = 1

    if (number <= 0 or number > 64):
        raise ValueError("square must be between 1 and 64")

    if(number == 1):
        return 1
    elif (number > 0):
        for i in range(number - 1):
            acumulador *= 2

    return acumulador

def total():
    acumulador = 0
    for i in range(64):
        acumulador += square(i + 1)
    return acumulador
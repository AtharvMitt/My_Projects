def Factorial(value):
    if value == 1:
        return 1
    return value * Factorial(value - 1)

print(Factorial(4))
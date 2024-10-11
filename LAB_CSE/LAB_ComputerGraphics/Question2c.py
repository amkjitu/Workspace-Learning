def divide_numbers(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("The division by zero operation is valid")
numerator = 100
denominator = 0
divide_numbers(numerator, denominator)

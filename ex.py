try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
else:
    print("The result of the division is:",result)
finally:
    print("The block will always execute, regardless of whether an exception")
print("Program continues after the exception handling the exception")



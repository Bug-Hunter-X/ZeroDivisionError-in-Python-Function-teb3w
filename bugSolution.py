def my_function(x):
    if x == 0:
        return 0 # or raise an exception: raise ZeroDivisionError("Cannot divide by zero")
    else:
        return 1 / x

print(my_function(0))
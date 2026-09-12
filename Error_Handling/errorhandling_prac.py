# division of two number and handling errors


def divide(first, second):
    print(" ***Program run succesfull !*** ")
    try:
        a = int(first)
        b = int(second)
        result = a / b
    except ValueError as e:
        print(f" ERROR : {e}")
        return None
    except ZeroDivisionError as e:
        print(f" ERROR : {e}")
        return None
    return result


result = None
while result == None:

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = divide(num1, num2)
    if result == None:
        print(" \n * \n * \n incorrect input !! \n please enter correctly !")
print("Result:", result)

def divide(a , b):
    if isinstance( a , bool) or not isinstance(a , (int , float)):
        raise TypeError("a must be number !!!")
    if isinstance( b , bool) or not isinstance(b , (int , float)):
        raise TypeError("b must be number !!!")
    if b == 0 :
        raise ZeroDivisionError(" b must not be zero !!!")
    return a / b

def calculate(a, b, function):
    def add(a, b):
        return a+b
    def mul(a, b):
        return a*b
    def sub(a, b):
        return a - b
    def div(a , b):
        if b!=0:
            return a/b
        else :
            print('zero division ERROR')
            return None
    
    if function=='add':
        return add(a, b)
    if function=='mul':
        return mul(a, b)
    if function=='sub':
        return sub(a, b)
    if function=='div':
        return div(a, b)
    
    
print(calculate(3,4,'add'))
print(calculate(3,4,'mul'))
print(calculate(3,4,'sub'))
print(calculate(3,4,'div'))
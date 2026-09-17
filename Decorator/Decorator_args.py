#this is exactly Decorator.py but here i try args and for parameter.

import time

def run_time(f):
    def wrapper(*args):
        start = time.perf_counter()
        result = f(*args)
        end = time.perf_counter()
        print(f'Runtime was : {end - start}')
        return result
    return wrapper

@run_time
def make_list(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    return l

@run_time
def make_list_exactly(s , i , b):
    info = []
    info.append(s)
    info.append(i)
    info.append(b)
    return info

n = int(input('enter length of your list : '))

l = make_list(n)
print(l)

print(make_list_exactly('ali',23,True))

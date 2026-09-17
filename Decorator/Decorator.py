'''
> **Decorator Exercise**
>
> Write a decorator that calculates the execution time of a function and displays it after 
    the function finishes executing. Then, use this decorator with a function that creates 
    a list of numbers from 1 to n.
>
> **Input:**
> An integer `n` that specifies the size of the list.
>
> **Output:**
>
> * The return value of the function (a list from 1 to n)
> * The function's execution time in seconds
'''

# one argument positional

import time

def run_time(f):
    def wrapper(n):
        start = time.perf_counter()
        result = f(n)
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

n = int(input('enter length of your list : '))

l = make_list(n)
print(l)
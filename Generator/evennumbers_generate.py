def even_numbers(n):
    number = 0
    while n >= number:
        yield number
        number += 2

for number in even_numbers(10):
    print(number)


print('')       # empty line for sep

number = even_numbers(16)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
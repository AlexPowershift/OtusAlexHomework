
def power_numbers(*args):

    t = []
    for num in args:
        t.append(num ** 2)
    return t

print(power_numbers(1,2,5,7))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(*args, filter):
    if filter == 'even':
        return [number for number in args if number % 2 == 0]
    elif filter == 'prime':
        return [number for number in args]
    elif filter == 'odd':
        return [number for number in args if number % 2 != 0]

print(filter_numbers(1,2,3,4,5,6,7,8,9,10, filter = 'odd'))
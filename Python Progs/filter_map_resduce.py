# def is_even(n):
#     return n % 2 == 0
from functools import reduce

nums = [3, 2, 6, 8, 4, 2, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n*2, evens))
sums = reduce(lambda a,b: a+b, doubles)
print(evens)
print(doubles)
print(sums)

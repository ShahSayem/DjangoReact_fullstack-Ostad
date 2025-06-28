from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda n: n%2 == 0, nums))

print(even_nums)

sq_even_nums = list(map(lambda n: n**2, even_nums))
print(sq_even_nums)

sum_of_nums = reduce(lambda x, y: x+y, nums)
print(sum_of_nums)
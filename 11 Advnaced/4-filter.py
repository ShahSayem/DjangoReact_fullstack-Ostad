def is_even(num):
    return num%2 == 0


print(is_even(4))
print(is_even(5))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = filter(is_even, nums)
print(list(even_nums))
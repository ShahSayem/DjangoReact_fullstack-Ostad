def map_func(x):
    return x*5 + 30


list1 = [1, 5, 8, 30, 43]
calc_map = map(map_func, list1)

print(list(calc_map))
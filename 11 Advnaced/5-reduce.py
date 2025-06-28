from functools import reduce

def mul(x, y):
    return x*y


nums = [1, 2, 3, 4, 5]
    #(((((1*2)*3)*4)*5) = 120
products = reduce(mul, nums)

print(products)
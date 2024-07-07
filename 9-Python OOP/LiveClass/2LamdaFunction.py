def getting(name):
    return f"Hello, {name}! from normal func"

print(getting("Shah_Sayem"))


#Lamda Func

#lambda arguments : expression
greet = lambda name: f"Hello, {name}! from lambda func"
print(greet("Shah_Sayem"))


nums = [1, 2, 3, 4, 5]
doubledNums = list(map(lambda x: x*2, nums))
print(doubledNums)


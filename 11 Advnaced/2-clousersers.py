def outer_function(x):
    def inner_function(y):
        return x+y
    
    return inner_function

add_five = outer_function(5)
print(add_five(3))

print(add_five(4))
print("\n######################\n")


#counter using clouser

def make_counter():
    cnt = 0
    def counter():
        nonlocal cnt
        cnt +=1
        return cnt

    return counter

counter1 = make_counter()

print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())
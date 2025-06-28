def outer_function(name):
    def inner_function():
        return f"Hello {name}"
    
    return inner_function()

print(outer_function("Shah Sayem"))
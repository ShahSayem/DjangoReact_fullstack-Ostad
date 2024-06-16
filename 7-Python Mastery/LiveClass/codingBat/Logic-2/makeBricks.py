def make_bricks(small, big, goal):
    if (big*5 >= goal):
        goal %= 5
    else:
        goal -= (big*5)

    return (goal <= small)
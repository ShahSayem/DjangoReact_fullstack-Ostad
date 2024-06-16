def sum67(nums):
    start= False
    sum = 0

    for curr in nums:
        if (curr == 6):
            start = True
        elif (start and curr == 7):
            start = False
        elif(start == False):
            sum += curr

    return sum
        
    
# nums = [1, 2, 2, 6, 99, 7]
nums = [1, 1, 6, 7, 2]
print(sum67(nums))
        
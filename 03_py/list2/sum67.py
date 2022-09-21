# https://codingbat.com/prob/p108886

"""
Return the sum of the numbers in the array, except ignore sections of numbers
starting with a 6 and extending to the next 7 (every 6 will be followed by at
least one 7). Return 0 for no numbers.
"""
def sum67(nums):
    sum = 0
    on = True
    for i in range(len(nums)):
        if(nums[i] == 6):
            on = False
        
        if(on):
            sum += nums[i] 
        
        if(nums[i] == 7):
            on = True
        
    return sum

# test cases: do not edit
print(sum67([1, 2, 2])) # 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 1, 6, 7, 2])) # 4


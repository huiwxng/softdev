# https://codingbat.com/prob/p167025

"""
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come
immediately after a 13 also do not count.
"""
def sum13(nums):
    # sum = 0
    # for i in range(len(nums)):
    #   if(nums[i] != 13 or (i > 0 and nums[i - 1] != 13)):
    #     sum += nums[i]
    # return sum
    
    # sum = 0
    # for num in nums:
    #   if (num == 13):
    #     return sum
    
    sum = 0
    i = 0
    while (i < (len(nums)) ):
        if (nums[i] == 13):
            i = i + 1
        else:
            sum += nums[i]
        i += 1
    return sum

# test cases: do not edit
print(sum13([1, 2, 2, 1])) # 6
print(sum13([1, 1])) # 2
print(sum13([1, 2, 2, 1, 13])) # 6


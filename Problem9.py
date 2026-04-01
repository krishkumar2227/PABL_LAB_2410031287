#9.Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution and you may not use the same element twice.
def two_sum(nums, target):
    hashmap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[num] = i


# Example
nums = [2, 7, 11, 15]
target = 9

print("Indices:", two_sum(nums, target))
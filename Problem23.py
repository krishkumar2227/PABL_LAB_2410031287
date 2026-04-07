#23.Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.If target is not found in the array, return [-1, -1].You must write an algorithm with O(log n) runtime complexity.
def searchRange(nums, target):
    
    def findFirst(nums, target):
        low, high = 0, len(nums) - 1
        first = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                first = mid
                high = mid - 1   # move left
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return first

    def findLast(nums, target):
        low, high = 0, len(nums) - 1
        last = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                last = mid
                low = mid + 1   # move right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return last

    return [findFirst(nums, target), findLast(nums, target)]
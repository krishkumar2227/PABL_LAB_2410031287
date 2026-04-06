#19.Given an integer array nums of unique elements, return all possible subsets (the power set.The solution set must not contain duplicate subsets.Return the solution in any order.
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])   # store current subset
        
        for i in range(start, len(nums)):
            path.append(nums[i])          # choose
            backtrack(i + 1, path)        # explore
            path.pop()                    # undo

    backtrack(0, [])
    return result
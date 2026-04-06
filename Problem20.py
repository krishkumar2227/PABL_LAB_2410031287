#20.Given an m x n grid of characters board and a string word, return true if word exists in the grid.The word can be constructed from letters of sequentially adjacent cells,where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
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
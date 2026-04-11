#30.given an integer array nums of unique elements,return all possible subsets(the power set) the solution set must not contain duplicate subsets.Return the solution in any order.
def subsets(nums):
    result = []

    def backtrack(index, current):
        # Add current subset
        result.append(current[:])

        for i in range(index, len(nums)):
            # include element
            current.append(nums[i])

            # move forward
            backtrack(i + 1, current)

            # backtrack (remove element)
            current.pop()

    backtrack(0, [])
    return result


# Example
nums = [1, 2, 3]
print(subsets(nums))
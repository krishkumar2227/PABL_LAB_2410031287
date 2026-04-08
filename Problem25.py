#25.Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You The same number may be chosen from candidates an unlimited number of times.The same number may be chosen from candidates an unlimited number of times.
def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])   # choose
            backtrack(i, path, remaining - candidates[i])  # reuse same element
            path.pop()   # backtrack

    backtrack(0, [], target)
    return result
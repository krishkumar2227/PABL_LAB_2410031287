#12.Given an array of distinct integers candidates and a target integer target, return a list of  all unique combinations of candidates where the chosen numbers sum to target. You may return the combination in any order.The same number may be choosen from candidates an unlimited number of times.Two combinations are unique if the frequency of at least one of the chosen number is different.
def combinationSum(candidates, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return result
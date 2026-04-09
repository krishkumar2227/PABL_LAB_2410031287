#26.Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.Each number in candidates may only be used once in the combination.Note: The solution set must not contain duplicate combinations.
def combinationSum2(candidates, target):
    result = []
    candidates.sort()
    
    def backtrack(start, path, target):
        if target == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            # skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            # stop if number is greater than target
            if candidates[i] > target:
                break
            
            path.append(candidates[i])
            backtrack(i + 1, path, target - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result

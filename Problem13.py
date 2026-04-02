#13.Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.Each number in candidate.
def combinationSum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path)
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            # skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            backtrack(i + 1, path + [candidates[i]], total + candidates[i])

    backtrack(0, [], 0)
    return result
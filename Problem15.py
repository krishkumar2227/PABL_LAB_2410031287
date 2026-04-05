#15.Given an array of strings strs, group the anagrams together. You can return the answer in any order.
def groupAnagrams(strs):
    ans = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))  # sort string
        
        if sorted_word not in ans:
            ans[sorted_word] = []
        
        ans[sorted_word].append(word)

    return list(ans.values())
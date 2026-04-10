#28.Given an array of strings strs, group the anagrams together. You can return the answer in any order.Example 1:Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
def groupAnagrams(strs):
    d = {}
    
    for word in strs:
        key = ''.join(sorted(word))
        
        if key not in d:
            d[key] = []
        
        d[key].append(word)
    
    return list(d.values())
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = defaultdict(list)

        for i in strs:
            cache["".join(sorted(i))].append(i)
        
        return [x[1] for x in cache.items()]


"""
initialize dictionary "sorted" -> list

iterate through strs
    sort it in order and add to dict

return values of dictionary

"""
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        first = min(strs)
        last = max(strs)
      
        length = min(len(first), len(last))

        for idx in range(length):
            if first[idx] != last[idx]:
                return first[0:idx]

        return first[0:length]
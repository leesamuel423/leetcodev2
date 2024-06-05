class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      res = ""
      for idx, letter in enumerate(strs[0]):
        
        for i in strs:
          if idx >= len(i) or i[idx] != letter:
            return res
        res += letter
      return res

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        final = 0
        cache = {}

        while right < len(s):
            curr = s[right]
            if curr not in cache or cache[curr] < left:
                cache[curr] = right
            else:
                final = max(final, right - left)
                left = cache[curr] + 1
                cache[curr] = right
            right += 1
        
        final = max(final, right - left)

        return final

"""
sliding window problem
initialize left and right at 0
final initialized to 1
cache = {
    alphabet: index
}

while right < len(s):
    if right no in cache or right[cache] < left: 
        cache[curr right letter] = right idx
    elif in cache:
        final = max between final and right - left
        left = cache[curr right letter] + 1

return final
"""
        

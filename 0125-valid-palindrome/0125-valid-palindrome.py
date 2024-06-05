class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        if len(s) == 0 or len(s) == 1:
            return True
        return s == s[::-1]

"""
pointer1 -> start
pointer2 -> end

while p1 < p2
    if p1 is a letter and p2 is a letter and they are the same
    if not the same, return false
    while p1 is not a letter, p1++
    while p2 is not a letter, p2 --

return true
"""

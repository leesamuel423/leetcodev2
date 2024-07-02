from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cache = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not len(digits):
            return []

        final = []

        def helper(idx, slate = []):
            # Base Case
            if idx >= len(digits):
                final.append("".join(slate))
                return

            for i in cache[digits[idx]]:
                slate.append(i)
                print(i, slate)
                helper(idx + 1, slate)
                slate.pop()

        helper(0, [])
        return final
        

"""
create a dictionary of num and corresponding letters
dict = {num: [letter]}

recursive helper function (curr_idx, slate = [])
    Base Case: curr_idx >= len(digits):
        push slate to final
    
    for i in current index
        call recursive function with i added to slate
        pop from slate
"""
        
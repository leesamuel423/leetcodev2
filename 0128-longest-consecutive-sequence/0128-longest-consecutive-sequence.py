class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pruned = set(nums)
        output = 0

        for i in pruned:
            if i - 1 not in pruned:
                curr_max = 1
                curr_val = i
                while curr_val + 1 in pruned:
                    curr_max += 1
                    curr_val += 1
                output = max(output, curr_max)
        return output


from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque([])

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                queue.append(i)
                i += 1
            elif queue:
                zero = queue.popleft()
                nums[i], nums[zero] = nums[zero], nums[i]
            else:
                i += 1

        return nums
        


"""
[0, 0, 0, 0, 0, 1]
iterate through nums:
    keep a deque that holds zero positions as you go through
    once you get to nonzero, swap locations with leftpop of deeque and current location

"""
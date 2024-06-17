class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        count = 0

        for i in range(len(nums) - 1, 1, -1):
            curr = nums[i]
            desired = curr - diff
            if desired in nums_set and desired - diff in nums_set:
                count += 1

        return count 
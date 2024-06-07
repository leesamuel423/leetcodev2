class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for left in range(len(nums) - 2):
            if left > 0 and nums[left - 1] == nums[left]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                total = nums[left] + nums[mid] + nums[right]
                if total == 0:
                    output.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid + 1] == nums[mid]:
                        mid += 1
                    while mid < right and nums[right - 1] == nums[right]:
                        right -= 1
                    mid += 1
                    right -= 1
                elif total < 0:
                    mid += 1
                else:
                    right -= 1
        return output
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      cache = {}
      for i, val in enumerate(nums):
        remainder = target - val
        if remainder in cache:
          return [i, cache[remainder]]
        cache[val] = i


"""
initialize map

iterate (i) through nums:
  remainder = target - nums[i]
  if remainder in map, return [i, map.getRemainder]
  otherwise, add to map num, index

"""
        
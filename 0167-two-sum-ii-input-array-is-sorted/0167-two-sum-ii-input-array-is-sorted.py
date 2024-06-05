class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while True:
            sum = numbers[p1] + numbers[p2]
            if sum > target:
                while numbers[p2] == numbers[p2 - 1]:
                    p2 -= 1
                p2 -= 1
            elif sum < target:
                while numbers[p1] == numbers[p1 + 1]:
                    p1 += 1
                p1 += 1
            elif sum == target: 
                return [p1 + 1, p2 + 1]

"""
constant space complexity -> pointers

p1 = start
p2 = end

while loop
    sum = p1 value + p2 value
    if sum > target: decrease p2 
    if sum < target: increase p1
    if sum == target, return output
"""

        
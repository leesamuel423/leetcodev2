class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        output = float("-inf")

        while p1 < p2:
            curr = min(height[p1], height[p2]) * (p2 - p1)
            output = max(output, curr)
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
                
        return output
        

"""
[1, 1] -> brackets are not containers

p1 -> 0
p2 -> len(height) - 1
output = -inf

while p1 < p2:
    amount of water held = min(p1 vs p2) * (p2 - p1)
    replace output with max of output vs curramount of water held
    move smaller section of the p1 vs p2


"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) == 0:
            return []
        final = [len(heights) - 1]
        top = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            curr = heights[i]
            if curr > top:
                final.append(i)
                top = curr
        return final[::-1]



"""
max will be arr[-1] to begin
final = []

iterate from the right
    new max if bigger and add to final
    otherwise, assign new max

"""
        
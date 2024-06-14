class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        output = 0
        prefix = [float('inf')] * len(arr)
        minimum = float('inf')

        for i in range(len(arr) - 1 , -1, -1):
            minimum = min(minimum, arr[i])
            prefix[i] = minimum

        # print(prefix)

        maximum = float("-inf")

        for i in range(len(arr) - 1):
            maximum = max(maximum, arr[i])
            if maximum <= prefix[i + 1]:
                output += 1

        return output + 1





"""
element on left is less than or greater than element on right

"""
        
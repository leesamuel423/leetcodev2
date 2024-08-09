class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, nums, slate, output):
            if i == len(nums):
                output.append(slate[:])
                return
                
            
            dfs(i + 1, nums, slate, output)
            slate.append(nums[i])
            dfs(i + 1, nums, slate, output)
            slate.pop()
        
        output = []
        dfs(0, nums, [], output)
        return output

        
        
"""
create dfs helper function w/ slate, index, and output = []
    base case: if index == len(nums), append copy of slate to output and return

    dfs(index + 1) with slate unchanged
    add to slate nums[idx]
    dfs(idx + 1 with new slate)
    pop from slate

dfs with idx = 0, output = [], and emtpy slate = []

return output
"""
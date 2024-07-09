# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      def dfs(node):
        if not node:
          return 0, True  
        left, is_left_balanced = dfs(node.left)
        right, is_right_balanced = dfs(node.right)

        if not is_left_balanced or not is_right_balanced:
          return 0, False
        
        if abs(left - right) > 1:
          return 0, False

        return max(left, right) + 1, True

      _, isBalanced = dfs(root)
      return isBalanced
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        cache = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            curr, col = queue.popleft()
            cache[col].append(curr.val)
            
            if curr.left:
                queue.append((curr.left, col - 1))
            if curr.right:
                queue.append((curr.right, col + 1))

        return [x[1] for x in sorted(cache.items())]


"""
traverse through binary search tree and add (column, row) and order by which column

we could do bfs or dfs
essentially go by level
bfs -> 3(0,0), 9(-1, 1), 8(1, 1), 4(-2,2), 0(0, 2), 1(0, 2), 7(2, 2)

cache = {list}
initialize deque

while queue exists:
    current = popleft from queue
    add to cache[column]
    if there is left: add to queue
    if there is right: add to queue

return cache values in []
"""
        
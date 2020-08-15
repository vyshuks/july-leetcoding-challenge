"""
Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # (root, depth, pos)
        queue = [(root, 0, 0)]
        currentDepth = result = left = 0
        for root, depth, pos in queue:
            if root:
                queue.append((root.left, depth + 1, pos * 2))
                queue.append((root.right, depth + 1, pos * 2 + 1))
                # travel into new depth
                if currentDepth != depth:
                    currentDepth = depth
                    # when goes into a new depth, the left pos goes before right pos
                    left = pos
                else:
                    result = max(result, pos - left + 1)
        return result
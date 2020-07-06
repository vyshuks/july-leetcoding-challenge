"""
Given a binary tree, return the bottom-up level order traversal
of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result

        Q = []
        Q.append(root)
        while len(Q) > 0:
            nodes = []
            for i in range(len(Q)):
                node = Q.pop(0)
                nodes.append(node.val)
                if node.left != None:
                    Q.append(node.left)
                if node.right != None:
                    Q.append(node.right)

            result.insert(0, nodes)

        return result
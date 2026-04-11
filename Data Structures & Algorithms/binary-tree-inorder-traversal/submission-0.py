# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_sol(self,root,arr):
        if root is None:
            return
        self.recursive_sol(root.left,arr)
        arr.append(root.val)
        self.recursive_sol(root.right,arr)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.recursive_sol(root,arr)
        return arr

        
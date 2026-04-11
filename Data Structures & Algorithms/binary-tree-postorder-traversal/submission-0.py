# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive_sol(self,root,arr):
        if root is None:
            return None
        self.recursive_sol(root.left,arr)
        self.recursive_sol(root.right,arr)
        arr.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.recursive_sol(root,arr)
        return arr
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ##preorder , the value is read first and then the left and right branches are explored
    def recursive_sol(self,root,arr):
        if root is None:
            return
        arr.append(root.val)
        self.recursive_sol(root.left,arr)
        self.recursive_sol(root.right,arr)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.recursive_sol(root,arr)
        return arr
        
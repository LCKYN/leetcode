# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def d(r):
            
            if(r == None):
                return 0
            
            if(r.left != None) and (r.right != None):
                return max(d(r.left), d(r.right)) + 1
            
            if(r.left != None):
                return d(r.left) + 1
            
            if(r.right != None):
                return d(r.right) + 1
            return 0
            
        if(root == None): return 0
        return d(root) + 1
        
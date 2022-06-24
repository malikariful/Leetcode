# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m=0
        
    def find_depth(self,node,m):
        if node == None:
            self.m = max(self.m,m)
        
        if node != None:
            m+=1
            self.find_depth(node.left,m)
            self.find_depth(node.right,m)
            
            
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.find_depth(root,0)
        return self.m

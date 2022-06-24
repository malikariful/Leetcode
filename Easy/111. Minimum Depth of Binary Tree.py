# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m=1000000
        
    def find_depth(self,node,m):
        # if node == None:
        #     print(m)
        #     self.m = min(self.m,m)
            
        if (node != None):
            if (node.left == None and node.right == None):
                if self.m > m+1:
                #we add 1 here because the leaf node is not visited yet and thus the leaf node is not added in the path
                    self.m = m+1
            m+=1
            self.find_depth(node.left,m)
            self.find_depth(node.right,m)
            
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.find_depth(root,0)
        if self.m ==1000000:
            self.m=0
        return self.m
        

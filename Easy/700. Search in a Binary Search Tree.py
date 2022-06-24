# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.r=[None]
            
    def search(self,node,val):
        if node != None:
            if node.val == val:
                self.r[0]=node
                
            elif node.val > val:
                self.search(node.left,val)
            else:
                self.search(node.right,val)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.search(root,val)
        return self.r[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s=[]
        
    def traverse(self,node)->List[int]:
        
        if node != None:
            self.traverse(node.left)
            self.traverse(node.right)
            self.s.append(node.val)
            
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.s

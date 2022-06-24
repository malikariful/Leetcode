# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def merge(self,node1,node2,node):
            
        if(node1 != None and node2 != None):
            node.val = node1.val + node2.val
        
        if (node1 == None and node2 != None):
            node.val=node2.val
        elif node2 == None and node1 != None:
            node.val = node1.val
        elif node1 == None and node2 == None:
            node=None
            return 
      
        if node1 != None and node2 != None:
            if node1.left != None or node2.left != None:
                node.left = TreeNode(0,None,None)
            
            self.merge(node1.left,node2.left,node.left)
        
        if node1 != None and node2 == None:
            if node1.left != None:
                node.left = TreeNode(0,None,None)
            self.merge(node1.left,None,node.left)
            
        if node1 == None and node2 != None:
            if node2.left != None:
                node.left = TreeNode(0,None,None)
            self.merge(None,node2.left,node.left)
               
        if node1 != None and node2 != None:
            if node1.right != None or node2.right != None:
                node.right = TreeNode(0,None,None)
            self.merge(node1.right,node2.right,node.right)
            
        if node1 != None and node2 == None:
            if node1.right != None:
                node.right = TreeNode(0,None,None)
            self.merge(node1.right,None,node.right)
        if node1 == None and node2 != None:
            if node2.right != None:
                node.right = TreeNode(0,None,None)
            self.merge(None,node2.right,node.right)
            
            
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        self.root = TreeNode()
        if root1 == None and root2 == None:
            self.root = None
        self.merge(root1,root2,self.root)
        return self.root
        

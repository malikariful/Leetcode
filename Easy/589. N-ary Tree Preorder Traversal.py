"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def __init__(self):
        self.s=[]
        
    def traverse(self,node:'Node'):
        if node != None:
            self.s.append(node.val)
        
        if node != None:
            for child in node.children:
                self.traverse(child)
            
            
        
    def preorder(self, root: 'Node') -> List[int]:
        self.traverse(root)
        return self.s

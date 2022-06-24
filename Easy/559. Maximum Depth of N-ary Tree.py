"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.m=0
        
        
    def depth(self,node,m):
        if node != None:
            m+=1
            print(m)
            for n in node.children:
                self.depth(n,m)
            
            self.m = max(self.m,m)
                
                
    def maxDepth(self, root: 'Node') -> int:
        self.depth(root,0)
        return self.m

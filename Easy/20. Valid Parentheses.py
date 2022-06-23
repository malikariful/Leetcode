class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack.append(s[0])
        print('pushed:',stack[-1])
        for p in s[1:]:
            if p in ['(','{','[']:
                stack.append(p)
                print('pushed:',stack[-1])
                
            if p in [')','}',']']:
                if(len(stack)==0):
                    return False
                
                if(p==')' and stack[-1]!='(' or p=='}' and stack[-1]!='{' or p==']' and stack[-1]!='['):
                    return False
            
                print('popped:',stack.pop())
                
            
        if len(stack) == 0:
            return True
        return False
                

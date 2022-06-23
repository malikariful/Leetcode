class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        sr=s[::-1]
        if(sr==s):
            return True
        return False
    

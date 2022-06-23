class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        prev=0
        for r in s:
            d=roman[r]
            total+=d
            if(prev<d):
                total+=-prev*2
            prev=d
        
        
        return total    
        

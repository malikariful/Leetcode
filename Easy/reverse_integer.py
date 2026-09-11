class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647
        min_int = -2147483648

        res = 0

        while x != 0:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            if res > max_int //10 or res == max_int //10 and digit > 7:
                return 0
            if res < int(min_int/10) or res == int(min_int/10) and digit < -8:
                return 0
            #check overflows
            res = res * 10 + digit
        
        return res

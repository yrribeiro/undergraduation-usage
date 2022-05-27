def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)                      USING STRING CASTING
#         sz = len(x_str)
        
#         for i in range(sz):
#             complement_idx = sz-i-1
#             if x_str[i] != x_str[complement_idx]:
#                 return False
            
#         return True

        if x<0 or (x%10 == 0 and x != 0):
            return False
        
        reversed_x = 0
        while x > reversed_x:
            reversed_x = (reversed_x*10) + (x%10)
            x /= 10
            
        return reversed_x == x or reversed_x == x/10
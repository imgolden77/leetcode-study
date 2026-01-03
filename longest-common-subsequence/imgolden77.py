#First trial solution using memoization and recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = {}
        
        def dp(left, right):
            count =0
            if (left, right) in res:
                return res[(left, right)]

            if -left > len(text1) or -right > len(text2):
                return 0

            if text1[left]==text2[right]:
                count = 1 + dp(left - 1, right - 1)
            else:
                count += max(dp(left-1, right), dp(left, right-1))
            
            res[(left, right)]=count
            
            return count
        
        return dp(-1, -1)
    
